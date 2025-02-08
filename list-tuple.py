def movie_ratings(movies):
    """Analyzes movie ratings and displays movies with an average rating of 6.0 or higher."""
    
    filtered_movies = []  # List to store movies with average rating >= 6.0
    
    for title, year, ratings in movies:
        if ratings:  # Ensure there are ratings to calculate an average
            avg_rating = sum(ratings) / len(ratings)  # Calculate the average rating
            if avg_rating >= 6.0:
                filtered_movies.append((title, year, avg_rating))
    
    # Display the results
    print("Movies with an average rating of 6.0 or higher:")
    for title, year, avg_rating in filtered_movies:
        print(f"{title} ({year}) - Average Rating: {avg_rating:.1f}"" *")
         #print({title}, {year},"-","Average Rating:",{avg_rating}," *" )


# Example list of movies (title, release year, list of ratings)
list_of_movies = [
  ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

# Run the function
movie_ratings(list_of_movies)