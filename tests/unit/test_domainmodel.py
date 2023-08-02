import pytest
from games.domainmodel.model import Publisher, Genre, Game, Review, User, Wishlist


class TestArtist:

    def test_construction(self):
        games_wishlist = Wishlist()
        games_wishlist.add_game(Game(1, "game1"))
        games_wishlist.add_game(Game(2, "game2"))
        games_wishlist.add_game(Game(3, "game3"))
        print(f"Game at index 0: {games_wishlist.select_game(0)}")
        print(f"Game at index 1: {games_wishlist.select_game(1)}")
        print(f"Game at index 2: {games_wishlist.select_game(2)}")

test = TestArtist()
test.test_construction()
