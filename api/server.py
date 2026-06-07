# api/server.py
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.chat import router as chat_router
from api.routes.config import router as config_router
from api.routes.health import router as health_router
from core.agent import IdolhubAgent
from core.config import load_config

logger = logging.getLogger("idolhub.api")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Initializing active configurations and agent for REST API server...")
    try:
        cfg = getattr(app.state, "cfg", None) or load_config()
        agent = IdolhubAgent(cfg)
        await agent.initialize()
        app.state.agent = agent
        app.state.cfg = cfg
        logger.info("Agent initialization complete. REST API lifespan ready.")
        yield
    finally:
        logger.info("Closing database memory connections for agent...")
        if hasattr(app.state, "agent"):
            await app.state.agent.close()
        logger.info("REST API lifespan cleanup complete.")

def create_app() -> FastAPI:
    cfg = load_config()
    app = FastAPI(title="idolhub API", lifespan=lifespan)
    app.state.cfg = cfg
    
    origins = cfg.api.cors_origins or ["*"]  # nosec nosem
    allow_credentials = "*" not in origins
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  # nosec nosem
        allow_credentials=allow_credentials,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    app.include_router(health_router)
    app.include_router(chat_router)
    app.include_router(config_router)
    
    return app

app = create_app()
