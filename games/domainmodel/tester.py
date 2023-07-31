from games.domainmodel.model import Game, Genre


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
main()