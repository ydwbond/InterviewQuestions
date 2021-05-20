
movies = []


def add_movie():
    title = input("please enter title\n")
    director = input("please enter director\n")
    year = input("please enter year\n")
    movies.append({"title": title,
                   "director": director,
                   "year": year
                   })
    print(f"successfully added movie {title}")


def list_movie():
    print(f"you have {len(movies)} movies in your collection \r")
    for movie in movies:
        print(f"{movie['title']}, directed by {movie['director']}, released in {movie['year']}")


def find_movie_by_title():
    title = input("please enter title\n")
    for movie in movies:
        if movie['title'] == title:
            print(f"found movie {title}")
            print(f"{movie['title']}, directed by {movie['director']}, released in {movie['year']}")
            break
    else:
        print(f"the movie {title} is not in your collection")


## first class function

user_actions = {
    "a": add_movie,
    "l": list_movie,
    "f": find_movie_by_title
}

while True:
    user_action = input('''
Please enter an action:
"a" to add
"l" to list
"f" to find by title
"q' to quit
    ''')
    if user_action == "q":
        break
    elif user_action in user_actions:
        act = user_actions[user_action]
        act()
    else:
        print("invalid action")
