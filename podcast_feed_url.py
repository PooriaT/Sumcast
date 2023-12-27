import requests

def get_podcast_rss_feed_url(podcast_name):
    base_url = "https://itunes.apple.com/search"
    params = {"media": "podcast", "term": podcast_name}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() 
        data = response.json()

        # Assuming the first result is the podcast you're looking for
        podcast = data.get("results", [])[0]

        if podcast:
            rss_feed_url = podcast.get("feedUrl")
            return rss_feed_url
        else:
            print("Podcast not found")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching podcast: {e}")


if __name__ == "__main__":
    # Example usage:
    podcast_name = "startalk"#"your-podcast-name"
    rss_feed_url = get_podcast_rss_feed_url(podcast_name)

    if rss_feed_url:
        print(f"Podcast RSS Feed URL: {rss_feed_url}")

