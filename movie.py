import pandas as pd
import random

# Load movies and ratings data
movies_data = pd.read_csv('movies.csv')
ratings_data = pd.read_csv('ratings.csv')

# Input genre
genre = input("Enter a genre: ")

# Filter movies by genre
movies_filtered = movies_data[movies_data['genres'].str.contains(genre)]

# Randomly select 10 unique movies
random_movies = random.sample(list(movies_filtered['title']), 10)

# Display movie ratings
print("Ratings:")
for movie in random_movies:
    # Get the movie ID from movies data
    movie_id = movies_data[movies_data['title'] == movie]['movieId'].iloc[0]

    # Filter ratings by movie ID
    ratings = ratings_data[ratings_data['movieId'] == movie_id]

    if not ratings.empty:
        # Calculate the average rating for the movie
        average_rating = ratings['rating'].mean()

        if pd.isnull(average_rating):
            # If there is no average rating available
            print(f"Movie: {movie} - Average Rating: NO RATING")
        else:
            # If there is an average rating available
            print(f"Movie: {movie} - Average Rating: {average_rating:.2f}")
    else:
        # If no ratings found for the movie
        print(f"Movie: {movie} - Average Rating: NO RATING")
