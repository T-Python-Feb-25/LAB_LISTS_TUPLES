def get_movies_lists():  # task 1
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

def calculate_average_rating(ratings):  # task 2
    average = sum(ratings) / len(ratings)  # Calculate the average by summing and dividing by the number of ratings
    return average

def display_movies(movies):  # task 3
    print("\nMovies with average rating 6.0 or higher:")
    count = 1  # To display movie number in the format
    for movie in movies:
        title, year, ratings = movie  # Unpack the movie tuple
        average_rating = calculate_average_rating(ratings)  # Calculate the average rating
        if average_rating >= 6.0:  # If the average rating is 6.0 or higher
            print(f"{count}. {title} ({year}) - Average rating: {average_rating:.2f} ★")  # Display the movie details
            count += 1  # Increase the movie count for the next movie

# This part of the code will run the whole process
movies = get_movies_lists()  # Get the list of movies from the user
display_movies(movies)  # Display movies with average rating 6 or higher