import os
from core.utils.podcast_feed_url import get_podcast_rss_feed_url
from core.utils.podcast_audio import download_podcast_audio, get_podcast_audio_url
from core.utils.transcribe import get_large_audio_transcription_on_silence
import time

def process_podcast_text(first_step) -> None:
    text_directory = "core/data/text"
    os.makedirs(text_directory, exist_ok=True)
    second_step = time.time()
    print(f"Podcast audio downloaded in {round(second_step - first_step, 2)} seconds.")
    whole_text = get_large_audio_transcription_on_silence("core/data/audio/podcast.mp3")
    with open(os.path.join(text_directory, "whole_text.txt"), "w", encoding="utf-8") as file:
        file.write(whole_text)
    print("Podcast Text generated successfully!")
    third_step = time.time()
    print(f"Podcast Text generated in {round(third_step - second_step, 2)} seconds.")

def main() -> None:
    print("Welcome to the Podcast Summary App!")
    podcast_name = input("Enter the name of the podcast:\n")
    episode_name = input("Enter the name of the episode:\n")
    first_step = time.time()
    podcast_url = get_podcast_rss_feed_url(podcast_name)
    if podcast_url:
        episode_audio_url = get_podcast_audio_url(podcast_url, episode_name)
        if episode_audio_url and "Failed to fetch data" not in episode_audio_url:
            download_podcast_audio(episode_audio_url)
            process_podcast_text(first_step)
        else:
            print("Failed to download podcast audio. Please try again later.")
    else:
        print("Failed to fetch podcast feed. Please try again later.")


if __name__ == "__main__":
    # For Test
    # startalk
    # Cosmic Queries – Galaxies GaloreS
    main()
