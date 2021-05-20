class Movie:
    def __init__(self, name, year, director):
        self.name = name
        self.year = year
        self.director = director

    def print_detail(self):
        print(f"Movie {self.name} is directed by {self.director} and released in {self.year}")


movie_collection = []

user_action = f"please choose from on of the following action \r a - add a new movie, \r " \
              f"l - list all the movies" \
              f"f - find a movie" \
              f"q - quit"
