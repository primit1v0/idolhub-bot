# api/server.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from core.config import load_config, AppConfig
from core.agent import IdolhubAgent

logger = logging.getLogger("idolhub.api")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Initializing active configurations and agent for REST API server...")
    try:
        cfg = load_config()
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
    app = FastAPI(title="idolhub API", lifespan=lifespan)
    
    cfg = load_config()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cfg.api.cors_origins or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    return app

app = create_app()
