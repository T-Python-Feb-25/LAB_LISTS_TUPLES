movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

def get_average(movie):
    return movie[2]
filter_movie = []
for title,year,rating in movies:
    average = sum(rating) / len(rating)
    if average >= 6.0:
        filter_movie.append((title,year,average))

filter_movie.sort(key=get_average, reverse=True)

for i, (title, year , average) in enumerate(filter_movie, start=1):
    print(f"{i}. {title} ({year}) - average rating : {average:.2f}★")