from fastapi import FastAPI, HTTPException
from app.core.middleware import register_middleware
from app.routers import health, users
from fastapi.responses import JSONResponse
from app.core.exceptions import register_exceptions

app = FastAPI(
    title="Nexus AI Backend",
    version="0.1.0",
    description="Production-ready AI Knowledge Workspace Backend",
)

register_middleware(app)
register_exceptions(app)    

app.include_router(health.router)
app.include_router(users.router)
