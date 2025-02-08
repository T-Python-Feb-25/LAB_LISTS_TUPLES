movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

def get_average(ratings):
    return sum(ratings) / len(ratings)

valid_movies = []

for movie in movies:
    title, year, ratings = movie
    average_rating = get_average(ratings)
    if average_rating >= 6.0:
        valid_movies.append((title, year, average_rating))

for i, (title, year, avg_rating) in enumerate(valid_movies, start=1):
    print(f"{i}. {title} ({year}) - Average rating: {avg_rating:.2f} *")
