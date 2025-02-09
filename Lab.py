movies = [
    ("The Shawshank Redemption", 1994),
    ("The Godfather", 1972),
    ("Pulp Fiction", 1994),
    ("The Dark Knight", 2008),
    ("Schindler's List", 1993),
    ("The Room", 2003)
]

movies_with_ratings = [] 

for title, year in movies:
    rating = []  

    while len(rating) < 6:
        user_input = input(f"Enter a valid integer ({len(rating) + 1}/6) for {title} ({year}): ")

        if user_input.isdigit():
            user_rate = int(user_input)
            if 1 <= user_rate <= 10:
                rating.append(user_rate)
            else:
                print("Error: Please enter a number from 1 to 10.")
        else:
            print("Error: Please enter a valid integer.")

    movies_with_ratings.append((title, year, rating))  


movie_ratings = []
for title, year, ratings in movies_with_ratings:
    avg_rating = sum(ratings) / len(ratings)
    if avg_rating >= 6.0:
        movie_ratings.append((title, year, avg_rating))


movie_ratings.sort(key=lambda x: x[2], reverse=True)


print("\nTop Rated Movies:")
for i, (title, year, avg_rating) in enumerate(movie_ratings, 1):
    print(f"{i}. {title} ({year}) - Average rating: {avg_rating:.2f} ")
