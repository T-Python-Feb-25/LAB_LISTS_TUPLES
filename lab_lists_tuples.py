movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

filter_movies = []

for title,release_year,ratings in movies:
    averge_rating = sum(ratings) / len(ratings)
    if averge_rating >= 6:
        filter_movies.append((title,release_year,round(averge_rating,2)))
        
filter_movies.sort(key=lambda x: x[2],reverse=True)
for i, (title,year,rating) in enumerate(filter_movies,start=1):
    print(f"{i}. {title} ({year}) - Avergate rating: {rating} ★")
    
    