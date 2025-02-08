#1. Accepts a list of movies, with each movie represented as a tuple containing the movie title, release year, and a list of user ratings.
#2. Calculates the average rating for each movie.
##3. Filters out movies with an average rating lower than 6.0.
#5. Displays the  movies, along with their title, release year, and average rating.

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

for movie_title, release_year, user_ratings in movies:
    average_rating = sum(user_ratings) / len(user_ratings)  
    if average_rating < 6.0:
        continue  
    else:
        print(f"{movie_title} ({release_year}) - Average rating: {round(average_rating, 2)} ★ ")
        


movies_with_ratings = []

for movie_title, release_year, user_ratings in movies:
    average_rating = sum(user_ratings) / len(user_ratings)  
    if average_rating >= 6.0:  
        movies_with_ratings.append((movie_title, release_year, average_rating))
movies_with_ratings.sort(key=lambda x: x[2], reverse=True)

for (movie_title, release_year, avg_rating) in movies_with_ratings:
    print(f"{movie_title} ({release_year}) - Average rating: {round(avg_rating, 2)} ★ ")