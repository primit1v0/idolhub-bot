import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

from core.config import AppConfig
from core.agent import IdolhubAgent

logger = logging.getLogger(__name__)

class TelegramBot:
    def __init__(self, cfg: AppConfig):
        self.cfg = cfg
        self.agent = IdolhubAgent(cfg)
        
        # Validasi token
        if not self.cfg.telegram.token or "$" in self.cfg.telegram.token:
            raise ValueError("Token Telegram belum disetting dengan benar di environment!")

        self.app = (
            ApplicationBuilder()
            .token(self.cfg.telegram.token)
            .post_init(self._post_init)
            .post_stop(self._post_stop)
            .build()
        )

        # Daftarkan handlers
        self.app.add_handler(CommandHandler("start", self._start_handler))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self._message_handler))

    async def _post_init(self, application):
        """Dipanggil setelah bot terinisiasi, untuk setup async memory."""
        await self.agent.initialize()

    async def _post_stop(self, application):
        """Dipanggil saat bot dimatikan, untuk menutup koneksi database dengan aman."""
        await self.agent.close()

    def _is_allowed(self, user_id: int) -> bool:
        """Cek apakah user diizinkan mengakses bot (whitelist)."""
        allowed = self.cfg.telegram.allowed_users
        if not allowed:
            return True  # Jika kosong, semua diizinkan
        return user_id in allowed

    async def _start_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handler untuk command /start."""
        user = update.effective_user
        if not self._is_allowed(user.id):
            logger.warning(f"Akses ditolak untuk user: {user.id} ({user.username})")
            return

        welcome_text = (
            f"Halo {user.first_name}! Saya adalah idolhub personal assistant.\n"
            f"Mode saat ini: {self.cfg.llm.provider} ({self.cfg.llm.model}).\n\n"
            f"Silakan ketik pertanyaan atau perintah Anda."
        )
        await update.message.reply_text(welcome_text)

    async def _message_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handler untuk memproses pesan teks dari user."""
        user = update.effective_user
        if not self._is_allowed(user.id):
            return

        user_text = update.message.text
        logger.info(f"Menerima pesan dari {user.username} ({user.id}): {user_text}")

        # Tampilkan indikator "typing..."
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')

        try:
            # 1. Masukkan ke PocketFlow Agent dengan memory context
            response = await self.agent.run(user_id=str(user.id), user_input=user_text)
            
            # 2. Kirim balasan ke user
            await update.message.reply_text(
                text=response,
                parse_mode=self.cfg.telegram.parse_mode
            )
        except Exception as e:
            logger.error(f"Error saat memproses pesan: {e}", exc_info=True)
            await update.message.reply_text("Maaf, terjadi kesalahan saat memproses permintaan Anda.")

    def run(self):
        """Mulai bot Telegram (blocking)."""
        logger.info(f"Memulai idolhub Telegram Bot (Provider: {self.cfg.llm.provider})...")
        self.app.run_polling()
