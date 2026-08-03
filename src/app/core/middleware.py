from fastapi import FastAPI
import time

def register_middleware(app: FastAPI):

    @app.middleware("http")
    async def log_requests(request, call_next):
        print(f"Incoming {request.method} {request.url.path}")

        response = await call_next(request)

        print(f"Outgoing {response.status_code}")

        return response

    @app.middleware("http")
    async def execution_time(request, call_next):
        start = time.perf_counter()

        response = await call_next(request)

        end = time.perf_counter()

        print(f"Execution Time: {(end-start)*1000:.2f} ms")

        return response