def recommend_movie(genre):

    recommendations = {
        "action" : ["Avengers", "John Wick", "Mad Max"],
        "comedy" : ["3 Idiots", "The Mask", "Hera Pheri"],
        "romantic" : ["Titanic", "The Nptebook", "DDLJ"],
        "horror" : ["Conjuring", "Insidious", "It"]
    }

    genre = genre.lower()

    if genre in recommendations:
        print("\nRecommended Movies:")
        for movie in recommendations[genre]:
            print("-", movie)
    else:
        print("Sorry! Genre not found.")

def main():
    print("🎬 Movie Recommendation System")
    print("Available genres: Action, Comedy, Romantic, Horror")

    user_genre = input("Enter your favorite genre: ")
    recommend_movie(user_genre)

if __name__ == "__main__":
    main()



