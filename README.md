# podcast_summary
This app helps you to summarize a podcast content. 

#  UNDER CONSTRUCTION

Required libraries:

feedparser -> the fetch the data from Podcast RSS 

pip3 install SpeechRecognition pydub

pip install openai-whisper

uvicorn.run('main:app', host="0.0.0.0", port=8000, workers=4)

python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload -> for development


curl -X POST -H "Content-Type: application/json" -d '{"podcast_name": "startalk", "episode_name": "This is Your Brain on social media with anna lembke, MD"}' http://localhost:8000/api/summarize/