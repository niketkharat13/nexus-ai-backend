from fastapi import FastAPI
from app.routers import health, users

app = FastAPI(
    title="Nexus AI Backend",
    version="0.1.0",
    description="Production-ready AI Knowledge Workspace Backend",
)

app.include_router(health.router)
app.include_router(users.router)
