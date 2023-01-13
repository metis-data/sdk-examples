from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapialchemycollector import setup, MetisInstrumentor, PlanCollectType
from app.api.main import router as api_router
from app.settings import Settings
from app.db import async_engine
import os
settings = Settings()
app = FastAPI(title="async-fastapi-sqlalchemy")

app.include_router(api_router, prefix="/api")


@app.get("/", include_in_schema=False)
async def health() -> JSONResponse:
    return JSONResponse({"message": "It worked!!"})

METIS_SERVICE_NAME = os.getenv('METIS_SERVICE_NAME')
METIS_API_KEY = os.getenv('METIS_API_KEY')
METIS_SERVICE_VERSION = os.getenv('METIS_SERVICE_VERSION')

instrumentation: MetisInstrumentor = setup(
    METIS_SERVICE_NAME,
    api_key=METIS_API_KEY,
    service_version=METIS_SERVICE_VERSION,
)

instrumentation.instrument_app(app, async_engine)


if __name__ == "__main__":
    import uvicorn
    port = os.getenv('PORT', 8000)
    uvicorn.run(app, host="0.0.0.0", port=port)
