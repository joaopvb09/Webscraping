import pandas as pd
import random

# Load the movie data from CSV
movies_data = pd.read_csv('movies.csv')

# Ask for user input genre
genre = input("Enter a genre: ")

# Filter movies based on the chosen genre
genre_movies = movies_data[movies_data['genres'].str.contains(genre)]

# Check if any movies are found for the given genre
if genre_movies.empty:
    print("No movies found for the given genre.")
else:
    # Set the random seed
    random.seed()

    # Select 10 random movies from the genre
    random_movies = genre_movies.sample(n=10)

    # Display the selected movies
    print("Random Movies:")
    for _, movie in random_movies.iterrows():
        print(f"Title: {movie['title']} - Genres: {movie['genres']}")
