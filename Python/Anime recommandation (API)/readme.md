# Anime Recommendation System

This project is an anime recommendation system that uses the [Jikan API](https://jikan.moe/) to fetch anime data based on a user's input mood (genre) and anime length (short, medium, or long). The system retrieves the top 10 anime matching the given criteria and displays their titles, ratings, and descriptions.

## Features

- Fetches anime recommendations based on mood (genre) and anime length.
- Filters anime by episode length:
  - Short (1-12 episodes)
  - Medium (13-25 episodes)
  - Long (26+ episodes)
- Handles various HTTP errors (400, 404, connection issues, etc.) during API requests.
- Fetches additional anime information such as genres and episodes from the Jikan API.
  
## Example Usage

```bash
Enter your mood (e.g., action, drama, comedy): action
Enter anime length (short, medium, long): medium

Title: Cowboy Bebop
Rating: 8.79
Description: In the year 2071, humanity has colonized several planets and moons in the solar system...
------------------------------
Title: Attack on Titan
Rating: 9.12
Description: Several hundred years ago, humans were nearly exterminated by Titans...
------------------------------
...
```

## Error Handling

The script has robust error handling for various cases:
- **400 Error**: Bad request when the API parameters are not correctly provided.
- **Connection Error**: If the network connection is lost or unstable.
- **Timeout Error**: When the API takes too long to respond.
- **Other Request Errors**: Generic error handling for other potential issues.

## Improvements

Several improvements have been made to the original code to enhance functionality and ensure reliability:

1. **Added Genre Fetching**:
   - The app now fetches available genres dynamically from the Jikan API.
   - The user-provided mood is checked against this list of genres to ensure valid input.

2. **Episode Filtering**:
   - The app includes the ability to filter anime based on episode length (`short`, `medium`, or `long`).

3. **Error Handling**:
   - Improved error handling for HTTP errors like 400 (Bad Request), connection issues, and timeouts.

4. **Dynamic Query Adjustments**:
   - The app automatically adjusts API queries based on user inputs, making the results more relevant.

## Code Explanation

Here’s a brief overview of the Python code and what each part does:

1. **Fetching Available Genres**:
   The `get_available_genres()` function retrieves available genres from the Jikan API and stores them in a dictionary format (`genre_name: genre_id`).

2. **Filtering Anime by Episode Length**:
   The `filter_by_length()` function filters anime based on the episode count. It uses predefined ranges for short, medium, and long anime.

3. **Fetching and Displaying Recommendations**:
   The `get_anime_recommendations()` function fetches anime recommendations based on the user's mood (genre) and length. It first filters by genre, then by the length of the anime.

4. **Main Execution**:
   The main block collects user input for mood and anime length, then calls the recommendation function and displays the results.

## Conclusion

This anime recommendation system provides an interactive way to explore anime based on mood and episode length. My First project with APIs taught me a lot about how to use the Jikan API efficiently, handle API errors, and filter results based on user input. Future enhancements could include adding more advanced filtering options, such as anime airing status, age ratings, and more detailed genre categorizations.