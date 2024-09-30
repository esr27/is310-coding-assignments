favorite_movies = [
    {
        "name": "The Matrix I",
        "release_year": 1999,
        "sequels": ["The Matrix II", "The Matrix III", "The Matrix IV"]
    },
    {
        "name": "Star Wars IV",
        "release_year": 1977,
        "sequels": ["Star Wars V", "Star Wars VI", "Star Wars VII", "Star Wars VIII", "Star Wars IX"],
        "prequels": ["Star Wars I", "Star Wars II", "Star Wars III"]
    },
    {
        "name": "Blade Runner 2049",
        "release_year": 2017
    },
    {
        "name": "Mad Max: Fury Road",
        "release_year": 2015
    },
    {
        "name": "Dune: Part One",
        "release_year": 2021,
        "sequels": ["Dune: Part Two"]
    },
    {
        "name": "Tenet",
        "release_year": 2020
    },
    {
        "name": "Joker",
        "release_year": 2019
    },
    {
        "name": "Parasite",
        "release_year": 2019
    }
]

def check_release(movie):
    if movie["release_year"] < 2000:
        print("This movie was released before 2000")
    else:
        print("This movie was released during or after 2000")
        return movie["name"]

recent_movies = []

for movie in favorite_movies:
    output = check_release(movie)
    if output is not None:
        recent_movies.append(movie)

print(recent_movies)
    