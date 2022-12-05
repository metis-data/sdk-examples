from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapialchemycollector import setup, MetisInstrumentor, PlanCollectType
from routes.posts import router
from schemas.models import HealthResponse
from database.connection import engine
app = FastAPI()

print(engine)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=router, prefix="/posts")


@app.get("/", response_model=HealthResponse)
async def health():
    return HealthResponse(status="Ok")

instrumentation: MetisInstrumentor = setup('<SERVICE_NAME>',
                      api_key='<API_KEY>',
                      service_version='<SERVICE_VERSION>'
                      )

instrumentation.instrument_app(app, engine)
