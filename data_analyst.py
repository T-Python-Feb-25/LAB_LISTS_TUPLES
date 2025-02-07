#Creat a taple
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

#creat a list to store filtered
filtered_movies = []

#  creat a Function to Calculates the average rating and filter.
def filter_movies(movies, min_rating):
    for movie in movies:
     title, year, ratings = movie
     if ratings: # Check if the ritings list is not empty
       average_riting = sum(ratings) / len(ratings) #Calclate the aveg riting

       if average_riting >= min_rating:
          filtered_movies.append((title, year , average_riting))
          print(f"{title} - Average Riting: {average_riting:.2f}")
          if average_riting >= min_rating:
             filtered_movies.append((title, year, average_riting))

#Filters out movies with an average rating lower than 6.0.
filter_movies(movies, 6.0)


#Displays the  movies
print("\nMovies with an average rating of 6.0 or higher: ")
for index, (title, year, average_riting) in enumerate(filtered_movies, start=1):

    print(f"{index}. {title} ({year}) - Average riting: {average_riting:.2f} ★")


# تمت اضافة بعض المزايا في الكود كمثل
# اضفت معالج للاخطاء مثل التحقق اذا كانت قايمة التقييم فارغه
# استخدمت داله لتجعل الكود اكثر تنظيم



        

      