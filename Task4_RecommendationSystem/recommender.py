import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("movies.csv")

# Convert genre text into vectors
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(movies["genre"])

# Compute similarity
similarity = cosine_similarity(genre_matrix)

# Recommendation function
def recommend(movie_name):
    movie_index = movies[movies["title"] == movie_name].index[0]
    scores = list(enumerate(similarity[movie_index]))

    # sort by similarity score
    sorted_movies = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nBecause you liked '{movie_name}', you may also like:\n")

    for i in sorted_movies[1:6]:
        print(movies.iloc[i[0]]["title"])

# User input
movie = input("Enter movie name: ")
recommend(movie)