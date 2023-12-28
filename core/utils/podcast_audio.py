import requests
import feedparser
import os

def get_podcast_audio_url(podcast_url, episode_name):
    episode_name = episode_name.lower()
    response = requests.get(podcast_url, timeout=5)
    link = None
    if response.status_code == 200:
        feed = feedparser.parse(response.text)
        for entry in feed.entries:
            if entry.title.lower() in episode_name:
                for link in entry.links:
                    if link.type == 'audio/mpeg':
                        link = link.href
        return link
    else:
        return f"Failed to fetch data. Status code: {response.status_code}"

def download_podcast_audio(episode_audio_url):
    response = requests.get(episode_audio_url, stream=True, timeout=5)
    response.raise_for_status()
    # If this code is tested solely, it needs to replce core with ..
    if not os.path.exists("core/data/audio"): 
        os.makedirs("core/data/audio", exist_ok=True)
    with open("core/data/audio/podcast.mp3", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
        print("Podcast audio downloaded successfully!")


# if __name__ == "__main__":
#     PODCAST_URL = "https://feeds.simplecast.com/4T39_jAj" #"your-podcast-url"
#     EPISODE_NAME = "Cosmic Queries – Galaxies Galore"
#     EPISODE_AUDIO_URL = get_podcast_audio_url(PODCAST_URL, EPISODE_NAME)
#     if EPISODE_AUDIO_URL and "Failed to fetch data" not in EPISODE_AUDIO_URL:
#         print(f"Podcast audio URL: {EPISODE_AUDIO_URL}")
#         download_podcast_audio(EPISODE_AUDIO_URL)
