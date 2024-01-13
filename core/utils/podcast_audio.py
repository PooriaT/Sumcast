import requests
import feedparser
import os
from .fuzzy_matching import fuzzy_match_with_threshold
from constants import BASE_AUDIO_PATH

def get_episode_audio_url(podcast_url, episode_name):
    episode_name = episode_name.lower()
    response = requests.get(podcast_url, timeout=5)

    if response.status_code == 200:
        feed = feedparser.parse(response.text)
        for entry in feed.entries:
            entry_lower = entry.title.lower()
            if fuzzy_match_with_threshold(episode_name, entry_lower, 93):
                for link in entry.links:
                    if link.type == 'audio/mpeg':
                        if ":" in entry.itunes_duration:
                            duration = list(map(int, entry.itunes_duration.split(':')))
                            duration_minutes = duration[0] * 60 + duration[1]
                        else:
                            duration_minutes = int(entry.itunes_duration)/60
                        return link.href, duration_minutes
        return None, 0
    else:
        return f"Failed to fetch data. Status code: {response.status_code}", 0

def download_episode_audio(episode_audio_url):
    response = requests.get(episode_audio_url, stream=True, timeout=5)
    response.raise_for_status()

    audio_directory = BASE_AUDIO_PATH
    os.makedirs(audio_directory, exist_ok=True)

    audio_file_path = os.path.join(audio_directory, "podcast.mp3")
    with open(audio_file_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    print("Podcast audio downloaded successfully!")
