import os
from .podcast_feed_url import get_podcast_rss_feed_url
from .podcast_audio import download_episode_audio, get_episode_audio_url
from .transcribe_whisper import transcribe_large_audio_with_whisper
from .gemini import summarizing

BASE_TEXT_PATH = "storage/temp/text/"
BASE_AUDIO_PATH = "storage/temp/audio/"

def process_podcast_text(podcast_name: str, episode_name: str) -> None:
    podcast_url = get_podcast_rss_feed_url(podcast_name)
    if podcast_url:
        episode_audio_url, episode_duration = get_episode_audio_url(podcast_url, episode_name)
        if episode_audio_url and "Failed to fetch data" not in episode_audio_url:
            download_episode_audio(episode_audio_url)
            print(f"You need to be patient. It takes time to process the audio. Please wait approximately for {int(episode_duration * 0.33)} minutes.")
            os.makedirs(BASE_TEXT_PATH, exist_ok=True)
            whole_text = transcribe_large_audio_with_whisper(f"{BASE_AUDIO_PATH}podcast.mp3")
            with open(os.path.join(BASE_TEXT_PATH, "whole_text.txt"), "w", encoding="utf-8") as file:
                file.write(whole_text)
            print("Podcast Text generated successfully!")
            summary = summarizing(os.path.join(BASE_TEXT_PATH, "whole_text.txt"), streaming=False)
            return {"text": summary.text}
        else:
            return {"error": "Failed to download podcast audio. Please try again later."}
    else:
        return {"error": "Failed to fetch podcast feed. Please try again later."}