'''Movie Ratings Analysis
Scenario: You have just been hired as a data analyst at a movie streaming platform. Your manager has given you a list of movies, each with a tuple containing the movie title, release year, and user ratings. The platform allows users to rate movies on a scale of 1 to 10. Your manager wants you to create a Python program that:

Accepts a list of movies, with each movie represented as a tuple containing the movie title, release year, and a list of user ratings.
Calculates the average rating for each movie.
Filters out movies with an average rating lower than 6.0.
Displays the movies, along with their title, release year, and average rating.
Example input:

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
Expected output:

1. The Shawshank Redemption (1994) - Avergae rating: 9.17 ★
2. The Godfather (1972) - Avergae rating: 8.83 ★
3. The Dark Knight (2008) - Avergae rating: 8.83 ★
4. Schindler's List (1993) - Avergae rating: 7.83 ★
5. Pulp Fiction (1994) - Avergae rating: 7.17 ★'''

def get_movies_lists(): #task 1
    movie_list = []  # List to store movie details
    while True:
        title = input("Write the title of the movie: (or write 'done' to finish) ")
        if title.lower() == 'done':  # Check if the user wants to finish
            break
        release_year = int(input("When was it released? "))  # Get the release year as an integer
        ratings_input = input("What were the user ratings for it? (separate with commas) ")
        
        # Convert the ratings input to a list of integers
        ratings = [int(rating) for rating in ratings_input.split(',')]
        
        # Append the movie details (title, release year, ratings) as a tuple to the movie list
        movie_list.append((title, release_year, ratings))
    
    return movie_list

def calculate_average_rating(ratings): #task 2
    average = sum(ratings) / len(ratings)  # Calculate the average by summing and dividing by the number of ratings
    return average

movies = get_movies_lists() 

# Function to display movies with average ratings of 6 or more
def display_movies(movies):
    print("\nMovies with average rating 6.0 or higher:")
    for movie in movies:
        title, year, ratings = movie  # Unpack the movie tuple
        average_rating = calculate_average_rating(ratings)  # Calculate the average rating
        if average_rating >= 6.0:  # If the average rating is 6.0 or higher
          print(f"Title: {title}, Year: {year}, Average Rating: {average_rating:.2f}")  # Display the movie details

movies = display_movies(movies)
print(movies)