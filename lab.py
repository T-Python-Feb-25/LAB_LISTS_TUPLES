movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1]),
]



def calcAverageAndDisplay(listOfMovies):
    '''
    Calculates the average rating for each movie and displays movies with an average rating of 6.0 or higher
    
    Args: 
        listOfMovies (list): A list of tuples, where each tuple contains the movie title (str),
        release year (int), and a list of user ratings (list of ints).

    Returns: 
        None: This function print the result
    '''

    sum = 0
    numbering = 1
    for tupleElement in listOfMovies:
        sum = 0 
        for rate in tupleElement[-1]:
            sum+= rate
        average = round(sum / len(tupleElement[-1]), 2)
        if (average < 6):
            continue
        print(f"{numbering}. {tupleElement[0]} ({tupleElement[1]}) - Average rating: {average} ★")
        numbering+=1


calcAverageAndDisplay(movies)

