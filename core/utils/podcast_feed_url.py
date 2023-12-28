import requests

def get_podcast_rss_feed_url(podcast_name):
    base_url = "https://itunes.apple.com/search"
    params = {"media": "podcast", "term": podcast_name}

    try:
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        podcast = data.get("results", [])[0]
        if podcast:
            return podcast.get("feedUrl")
        else:
            print("Podcast not found")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching podcast: {e}")


# if __name__ == "__main__":
#     # Example usage:
#     PODCAST_NAME = "startalk"#"your-podcast-name" "startalk"
#     extracted_rss_feed_url = get_podcast_rss_feed_url(PODCAST_NAME)

#     if extracted_rss_feed_url:
#         print(f"Podcast RSS Feed URL: {extracted_rss_feed_url}")
