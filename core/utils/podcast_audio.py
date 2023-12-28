import requests
import feedparser
import os

def get_podcast_audio_url(podcast_url, episode_name):
    episode_name = episode_name.lower()

    response = requests.get(podcast_url, timeout=5)
    
    if response.status_code == 200:
        feed = feedparser.parse(response.text)
        for entry in feed.entries:
            if entry.title.lower() in episode_name:
                for link in entry.links:
                    if link.type == 'audio/mpeg':
                        return link.href
        return None
    else:
        return f"Failed to fetch data. Status code: {response.status_code}"

def download_podcast_audio(episode_audio_url):
    response = requests.get(episode_audio_url, stream=True, timeout=5)
    response.raise_for_status()
   
    audio_directory = "core/data/audio" # .. -> core
    os.makedirs(audio_directory, exist_ok=True)

    audio_file_path = os.path.join(audio_directory, "podcast.mp3")
    with open(audio_file_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
        
    print("Podcast audio downloaded successfully!")


# if __name__ == "__main__":
#     PODCAST_URL = "https://feeds.simplecast.com/4T39_jAj" #"your-podcast-url"
#     EPISODE_NAME = "Cosmic Queries – Galaxies Galore"
#     EPISODE_AUDIO_URL = get_podcast_audio_url(PODCAST_URL, EPISODE_NAME)
#     if EPISODE_AUDIO_URL and "Failed to fetch data" not in EPISODE_AUDIO_URL:
#         print(f"Podcast audio URL: {EPISODE_AUDIO_URL}")
#         download_podcast_audio(EPISODE_AUDIO_URL)
