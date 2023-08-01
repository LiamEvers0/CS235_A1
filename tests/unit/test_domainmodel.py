import pytest
from games.domainmodel.model import Publisher, Genre, Game, Review, User, Wishlist


class TestArtist:

    def test_construction(self):
        game1 = Game(1, "Game1")
        game2 = Game(2, "Game2")
        game3 = Game(3, "Game3")
        user1 = User("useR1", "NeidBfL")
        user2 = User("user2", "FidVeNvl")
        user3 = User("user3", "BioeionbvnE")
        review1 = Review(user1, game1, 4, "good")
        review2 = Review(user1, game2, 3, "okay")
        review3 = Review(user1, game3, 5, "excellent")
        review4 = Review(user2, game1, 2, "awful")
        review5 = Review(user2, game2, 1, "terrible")
        review6 = Review(user2, game3, 2, "bad")
        review7 = Review(user3, game1, 5, "amazing")
        review8 = Review(user3, game2, 3, "decent")
        review9 = Review(user3, game3, 0, "horrendous")
        assert review1.user == user1
        assert str(review1.user) == "<User user1>"
        assert review1.game == game1
        assert str(review1.game) == "<Game 1, Game1>"
        assert review2.user == user1
        assert str(review2.user) == "<User user1>"
        assert review2.game == game2
        assert str(review2.game) == "<Game 2, Game2>"
        assert review3.user == user1
        assert str(review3.user) == "<User user1>"
        assert review3.game == game3
        assert str(review3.game) == "<Game 3, Game3>"
        assert review4.user == user2
        assert str(review4.user) == "<User user2>"
        assert review4.game == game1
        assert str(review4.game) == "<Game 1, Game1>"
        assert review5.user == user2
        assert str(review5.user) == "<User user2>"
        assert review5.game == game2
        assert str(review5.game) == "<Game 2, Game2>"
        assert review6.user == user2
        assert str(review6.user) == "<User user2>"
        assert review6.game == game3
        assert str(review6.game) == "<Game 3, Game3>"
        assert review7.user == user3
        assert str(review7.user) == "<User user3>"
        assert review7.game == game1
        assert str(review7.game) == "<Game 1, Game1>"
        assert review8.user == user3
        assert str(review8.user) == "<User user3>"
        assert review8.game == game2
        assert str(review8.game) == "<Game 2, Game2>"
        assert review9.user == user3
        assert str(review9.user) == "<User user3>"
        assert review9.game == game3
        assert str(review9.game) == "<Game 3, Game3>"



test = TestArtist()
test.test_construction()
