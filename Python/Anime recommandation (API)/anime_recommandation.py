import requests

def get_available_genres():
    try:
        genre_url = "https://api.jikan.moe/v4/genres/anime"
        response = requests.get(genre_url, params={"filter": "genres"})
        response.raise_for_status()

        genres = response.json().get("data", [])
        genre_dict = {genre['name'].lower(): genre['mal_id'] for genre in genres}

        print("Available genres:")
        for genre_name, genre_id in genre_dict.items():
            print(f"{genre_name.title()} (ID: {genre_id})")

        return genre_dict

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch genres: {e}")
        return {}

def filter_by_length(anime_list, anime_length):
    length_ranges = {
        "short": (1, 12),
        "medium": (13, 25),
        "long": (26, float("inf"))
    }
    min_eps, max_eps = length_ranges.get(anime_length, (0, float("inf")))

    filtered_anime = [anime for anime in anime_list if anime.get('episodes') and min_eps <= anime['episodes'] <= max_eps]
    return filtered_anime

def display_anime(anime_list):
    if not anime_list:
        print("No anime to display.")
        return
    for anime in anime_list:
        print(f"Title: {anime['title']}")
        print(f"Rating: {anime['score']}")
        print(f"Description: {anime['synopsis']}")
        print(f"Episodes: {anime.get('episodes', 'N/A')}")
        print(f"ID: {anime['mal_id']}")
        print("-" * 30)

def get_anime_recommendations(genre_id, anime_length):
    base_url = "https://api.jikan.moe/v4/anime"
    params = {
        "genres": genre_id,
        "type": "tv",
        "limit": 20
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        anime_list = response.json().get("data", [])
        if not anime_list:
            print("No anime found for the selected genre.")
            return []

        print(f"Fetched {len(anime_list)} anime from the API:")
        for anime in anime_list:
            print(f"Title: {anime['title']}, Episodes: {anime.get('episodes', 'N/A')}, Rating: {anime['score']}")

        filtered_anime = filter_by_length(anime_list, anime_length)
        if not filtered_anime:
            print(f"No {anime_length} anime found for the selected genre.")
            return []

        return filtered_anime[:10]
    
    except requests.exceptions.HTTPError as he:
        print(f"HTTP error occurred: {he}")
    except requests.exceptions.ConnectionError:
        print("Connection error occurred. Please check your Internet connection.")
    except requests.exceptions.Timeout:
        print("The request timed out. Try again later.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

def get_anime_episodes(anime_id, page=1):
    try:
        url = f"https://api.jikan.moe/v4/anime/{anime_id}/episodes"
        params = {"page": page}
        response = requests.get(url, params=params)
        response.raise_for_status()

        episodes = response.json().get("data", [])
        if not episodes:
            print(f"No episodes found for anime ID {anime_id}.")
            return []

        print(f"Fetched {len(episodes)} episodes from page {page}:")
        for episode in episodes:
            print(f"Episode {episode['mal_id']}: {episode['title']}")

        return episodes
    
    except requests.exceptions.HTTPError as he:
        print(f"HTTP error occurred: {he}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return []

if __name__ == "__main__":
    genres = get_available_genres()

    mood = input("Enter your mood/genre (e.g., action, drama, comedy): ").strip().lower()
    
    if mood not in genres:
        print(f"Genre '{mood}' not found. Please use a valid genre.")
    else:
        length = input("Enter anime length (short, medium, long): ").strip().lower()
        genre_id = genres[mood]

        recommendations = get_anime_recommendations(genre_id, length)
        display_anime(recommendations)

        view_episodes = input("Do you want to view episodes for any anime? (yes/no): ").strip().lower()
        
        if view_episodes == 'yes':
            anime_id = input("Enter the anime ID for which you want to view episodes: ").strip()
            page = input("Enter the page number (optional, default is 1): ").strip()

            try:
                anime_id = int(anime_id)
                page = int(page) if page else 1

                get_anime_episodes(anime_id, page)
            
            except ValueError:
                print("Invalid input. Please enter numeric values for anime ID and page.")
