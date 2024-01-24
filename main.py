# import os
# import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from core.utils.process import process_podcast_text
from core.utils.command_process import linux_process
from constants import BASE_TEXT_PATH

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# uvicorn.run('main:app', host="0.0.0.0", port=8000, workers=4)
# python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload -> for development

# @app.on_event("startup")
# async def startup_event():
#     asyncio.create_task(linux_process())

@app.post("/api/summarize/")
def get_summary(body: dict):
    podcast_name = body.get('podcast_name')
    episode_name = body.get('episode_name')
    client_id = body.get('client_id')
    summary = process_podcast_text(podcast_name, episode_name, client_id)
    return summary
