from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

def register_exceptions(app: FastAPI):
    @app.exception_handler(HTTPException)
    async def handler(request, exc):
        return JSONResponse(
            status_code= exc.status_code,
            content={
                "success": False,
                "message": exc.detail
            }
        )
    