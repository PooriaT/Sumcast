from core.utils.podcast_feed_url import get_podcast_rss_feed_url
from core.utils.podcast_audio import download_podcast_audio, get_podcast_audio_url

def main() -> None:
    print("Welcome to the Podcast Summary App!")
    podcast_name = input("Enter the name of the podcast:\n")
    episode_name = input("Enter the name of the episode:\n")
    podcast_url = get_podcast_rss_feed_url(podcast_name)
    if podcast_url:
        episode_audio_url = get_podcast_audio_url(podcast_url, episode_name)
        if episode_audio_url and "Failed to fetch data" not in episode_audio_url:
            download_podcast_audio(episode_audio_url)
        else:
            print("Failed to download podcast audio. Please try again later.")
    else:
        print("Failed to fetch podcast feed. Please try again later.")

if __name__ == "__main__":
    # For Test
    # startalk
    # Cosmic Queries – Galaxies Galore
    main()

