import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Data Collection
# Replace 'movies.csv' with your dataset file
movies_data = pd.read_csv('movies.csv')

# Step 2: Data Preprocessing
# (Perform any necessary data cleaning and preprocessing steps here)

# Step 3: Exploratory Data Analysis
# (Analyze the dataset and extract relevant insights)

# Step 4: Recommendation Algorithms


def content_based_recommendation(movie_title):
    # Compute cosine similarity matrix based on movie genres
    genre_matrix = pd.get_dummies(movies_data['genre'])
    similarity_matrix = cosine_similarity(genre_matrix)

    # Get the index of the queried movie title
    movie_index = movies_data[movies_data['title'] == movie_title].index[0]

    # Get similarity scores of all movies with the queried movie
    similarity_scores = list(enumerate(similarity_matrix[movie_index]))

    # Sort movies based on similarity scores
    sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Return top 5 similar movies (excluding the queried movie itself)
    top_similar_movies = []
    for i in range(1, 6):
        movie_id = sorted_movies[i][0]
        movie_title = movies_data['title'].iloc[movie_id]
        top_similar_movies.append(movie_title)
    return top_similar_movies

# Step 5: Model Training
# (No explicit model training is required for content-based filtering)

# Step 6: Model Evaluation
# (No explicit model evaluation is required for content-based filtering)

# Step 7: User Interface


def user_interface():
    while True:
        print("Enter a movie title (or 'quit' to exit):")
        movie_title = input()

        if movie_title.lower() == 'quit':
            break

        recommendations = content_based_recommendation(movie_title)

        print(f"\nRecommended movies for '{movie_title}':")
        for i, movie in enumerate(recommendations):
            print(f"{i+1}. {movie}")
        print()

# Step 8: Deployment
# (No explicit deployment steps provided in this example)

# Step 9: Testing and Improvements
# (Test the recommendation system and gather user feedback for improvements)


# Call the user interface function to run the program
user_interface()
