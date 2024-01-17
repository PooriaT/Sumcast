import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from core.utils.process import process_podcast_text
from core.utils.gemini import summarizing
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
# @app.get("/")
# def root():
#     with open("static/index.html", "r", encoding="utf-8") as file:
#         return HTMLResponse(file.read())

@app.post("/api/summarize/")
def get_summary(body: dict):
    podcast_name = body.get('podcast_name')
    episode_name = body.get('episode_name')
    client_id = body.get('client_id')
    summary = process_podcast_text(podcast_name, episode_name, client_id)
    return summary
