


def movieRatings(movies:list):
    count=0
    for tuplee in movies:
        for y in tuplee:
            if  isinstance(y, list):
                sum = 0
                final = 0
                for z in y:
                    sum += z
                    final = round(sum / len(y), 2)
                if final > 6.0:
                    count += 1
                    print(f"{count}. {tuplee[0]}-({tuplee[1]}) - Average Rating: {final} ★")


movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("Aquamarine", 2006, [1, 2, 5, 3, 5, 1]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

movieRatings(movies)











