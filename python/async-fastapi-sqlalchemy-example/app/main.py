from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapialchemycollector import setup, MetisInstrumentor, PlanCollectType
from app.api.main import router as api_router
from app.settings import Settings
from app.db import async_engine

settings = Settings()
app = FastAPI(title="async-fastapi-sqlalchemy")

app.include_router(api_router, prefix="/api")


@app.get("/", include_in_schema=False)
async def health() -> JSONResponse:
    return JSONResponse({"message": "It worked!!"})


instrumentation: MetisInstrumentor = setup(
    "<SERVICE_NAME>",
    api_key="gJhS2IRSo3vNLKb5VX9n3AaXYxPPXwE7ZmU1xO06",
    service_version="<SERVICE_VERSION>",
)

instrumentation.instrument_app(app, async_engine)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
