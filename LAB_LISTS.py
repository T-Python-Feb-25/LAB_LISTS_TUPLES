movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 9, 9, 9]),
    ("The Godfather", 1972, [8, 9, 9, 9, 9]),
    ("The Dark Knight", 2008, [9, 8, 9, 9, 9]),
    ("Schindler's List", 1993, [8, 8, 8, 8, 8]),
    ("Pulp Fiction", 1994, [7, 7, 7, 7, 7])
]

movies_with_avg = [
    (title, year, round(sum(rating) / len(rating) , 2)) for title, year, rating in movies
    if (sum(rating) / len (rating)) >= 6.0
        ]
for title, year, avg in movies_with_avg:
    print(f".{title} ({year}) - Average Rating: {avg:.2f} ★")

