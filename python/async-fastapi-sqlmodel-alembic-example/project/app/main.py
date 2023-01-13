from fastapi import Depends, FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapialchemycollector import setup, MetisInstrumentor, PlanCollectType
import os
from app.db import get_session, engine as async_engine
from app.models import Song, SongCreate

app = FastAPI()

METIS_SERVICE_NAME = os.getenv('METIS_SERVICE_NAME')
METIS_API_KEY = os.getenv('METIS_API_KEY')
METIS_SERVICE_VERSION = os.getenv('METIS_SERVICE_VERSION')

instrumentation: MetisInstrumentor = setup(
    METIS_SERVICE_NAME,
    api_key=METIS_API_KEY,
    service_version=METIS_SERVICE_VERSION,
)

instrumentation.instrument_app(app, async_engine)

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/songs", response_model=list[Song])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, year=song.year, id=song.id) for song in songs]


@app.post("/songs")
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_session)):
    song = Song(name=song.name, artist=song.artist, year=song.year)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song
