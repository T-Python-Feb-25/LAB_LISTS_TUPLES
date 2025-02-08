#function accept one variable (movies) its list included data for a number of movie ( title , year , ratings)
def movies_rating (movies):
    #create empty list for movies
    filtered_movies = []
    #loop for list of movies it dismantling every movie
    for title, year, ratings in movies:
        #to calculate the averge rating 
        avg_rating = sum(ratings) / len(ratings)
        if avg_rating >= 6.0:
            #function for add variable in the last to the list 
            filtered_movies.append((title, year, avg_rating))
    #here i use this function to sort and the key for make the vari positve and start from 2
    filtered_movies.sort(key=lambda x: x[2], reverse=True)
    #the list is passed by enumerate to add a sort order num to each movie start from 1
    for idx, (title, year, avg_rating) in enumerate(filtered_movies, start=1):
        print(f"{idx}. {title} ({year}) - Average rating: {avg_rating:.2f} ★")

#input list
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]


#he function
movies_rating(movies)
