from games.domainmodel.model import Game, Genre, Publisher


def main():
    game1 = Game(101, "  Rocket League")
    print(game1)
    genre1 = Genre("Action")
    genre2 = Genre("Multiplayer")
    genre3 = Genre("Esport")
    game1.add_genre(genre1)
    game1.add_genre(genre2)
    game1.add_genre(genre3)
    print(game1.genres)
    game1.remove_genre(genre2)
    print(game1.genres)
    game1.release_date = "Oct 21, 2008"
    print(game1.release_date)
    print(game1.game_id)
    print(game1.title)
    game1.description = "Game with cars"
    print(game1.description)
    publisher1 = Publisher("Psyonix")
    game1.publisher = publisher1
    print(game1.publisher)
    game1.image_url = "randomurl"
    print(game1.image_url)
    game1.website_url = "randomurl2"
    print(game1.website_url)
    game1.image_url = ""
    print(game1.image_url)
    game1.website_url = ""
    print(game1.website_url)


main()