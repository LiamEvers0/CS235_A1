import pytest
from games.domainmodel.model import Publisher, Genre, Game, Review, User, Wishlist


class TestArtist:

    def test_construction(self):
        publisher1 = Publisher("Publisher A")
        assert str(publisher1) == "<Publisher Publisher A>"
        publisher2 = Publisher("Publisher B")
        assert str(publisher2) == "<Publisher Publisher B>"
        publisher3 = Publisher("Publisher C")
        assert str(publisher3) == "<Publisher Psyonix>"
        game1 = Game(101, "Rocket League")
        assert str(game1) == "<Game 101, Rocket League>"
        genre1 = Genre("Action")
        genre2 = Genre("Multiplayer")
        game1.add_genre(genre1)
        game1.add_genre(genre2)
        assert str(game1.genres) == "[<Genre Action>, <Genre Multiplayer>]"
        game1.add_genre(genre1)
        assert str(game1.genres) == "[<Genre Action>, <Genre Multiplayer>]"
        game1.publisher = publisher3

        # TODO - the test will fail as the code is incomplete......


# TODO
test = TestArtist()
test.test_construction()
