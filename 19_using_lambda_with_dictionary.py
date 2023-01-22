movie_list = {
    1: {"name": "The Princess", "rating": 26},
    2: {"name": "Spider-Man: No Way Home", "rating": 81},
    3: {"name": "Morbius", "rating": 64},
    4: {"name": "The Northman", "rating": 72},
    5: {"name": "Troll", "rating": 67},
    6: {"name": "Avatar", "rating": 76},
    7: {"name": "The Woman King", "rating": 79}
}

def get_rating(movie_id):
    return movie_list[movie_id]["rating"]

sorted_by_rating = sorted(movie_list, key=get_rating, reverse=True)
sorted_by_rating_lambda = sorted(movie_list, key=lambda movie_id: movie_list[movie_id]["rating"], reverse=True)

for movie_id in sorted_by_rating_lambda:
    print(movie_list[movie_id])
