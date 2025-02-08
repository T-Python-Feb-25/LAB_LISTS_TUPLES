movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
movies_with_new_format=[]
for content in range(len(movies)):
    if sum(movies[content][2])/len(movies[content][2])>=6:
        movies_with_new_format.append((movies[content][0],movies[content][1],round(sum(movies[content][2])/len(movies[content][2]),2)))
movies_with_new_format.sort(key=lambda movies_with_new_format:movies_with_new_format[2],reverse=True)
for index in range(len(movies_with_new_format)):
    print(f"{index+1}. {movies_with_new_format[index][0]} ({movies_with_new_format[index][1]}) - Avergae rating: {movies_with_new_format[index][2]} ★")