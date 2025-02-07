def calculatingAvarageRatings (movies):
    result = []
    for title , releaseYear, ratings in movies:
        if ratings:
            averageRatings= sum(ratings)/len(ratings)
        else:
            averageRatings=0

        if averageRatings >= 6.0:
            result.append((title, releaseYear, averageRatings))

    return result
def displayMovies (movies):
    count=1
    for  title, releaseYear,averageRating in movies:
        print (count,end=". ")
        print (f" {title} ({releaseYear}) - Average Rating: {averageRating:.2f}★")
        count+=1


movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

filteredMovies = calculatingAvarageRatings(movies)
displayMovies(filteredMovies)