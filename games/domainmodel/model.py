import datetime


class Publisher:
    def __init__(self, publisher_name: str):
        if isinstance(publisher_name, str):
            publisher_name = publisher_name.strip()
            if publisher_name == "":
                self.__publisher_name = None
            else:
                self.__publisher_name = publisher_name
        else:
            self.__publisher_name = None

    @property
    def publisher_name(self) -> str:
        return self.__publisher_name

    @publisher_name.setter
    def publisher_name(self, new_publisher_name: str):
        if isinstance(new_publisher_name, str):
            new_publisher_name = new_publisher_name.strip()
            if new_publisher_name == "":
                self.__publisher_name = None
            else:
                self.__publisher_name = new_publisher_name
        else:
            self.__publisher_name = None

    def __repr__(self):
        # we use access via the property here
        return f"<Publisher {self.__publisher_name}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__publisher_name == other.publisher_name

    def __lt__(self, other):
        if isinstance(other, Publisher):
            return self.__publisher_name < other.__publisher_name

    def __hash__(self):
        return hash(self.__publisher_name)


class Genre:
    def __init__(self, genre_name: str):
        if isinstance(genre_name, str):
            genre_name = genre_name.strip()
            if genre_name == "":
                self.__genre_name = None
            else:
                self.__genre_name = genre_name
        else:
            self.__genre_name = None

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__genre_name == other.__genre_name

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.__genre_name < other.__genre_name

    def __hash__(self):
        return hash(self.__genre_name)


class Game:
    def __init__(self, game_id, game_title):
        if (not isinstance(game_id, int)) or game_id < 0:
            raise ValueError
        else:
            self.__game_id = game_id

        if isinstance(game_title, str):
            game_title = game_title.strip()
            if game_title == "":
                self.__game_title = None
            else:
                self.__game_title = game_title
        else:
            self.__game_title = None

        self.__game_price = None
        self.__game_genres = []
        self.__game_reviews = []
        self.__game_release_date = None
        self.__game_description = None
        self.__game_publisher = None
        self.__game_image_url = None
        self.__game_website_url = None

    @property
    def game_id(self) -> int:
        return self.__game_id

    @property
    def genres(self) -> list:
        return self.__game_genres

    @property
    def reviews(self) -> list:
        return self.__game_reviews

    @property
    def title(self) -> str:
        return self.__game_title

    @title.setter
    def title(self, new_game_title):
        if isinstance(new_game_title, str):
            game_title = new_game_title.strip()
            if game_title == "":
                self.__game_title = None
            else:
                self.__game_title = game_title
        else:
            self.__game_title = None

    @property
    def price(self) -> int:
        return self.__game_price

    @price.setter
    def price(self, new_price):
        if (not isinstance(new_price, int)) or new_price < 0:
            raise ValueError
        else:
            self.__game_price = new_price

    @property
    def release_date(self) -> str:
        return self.__game_release_date

    @release_date.setter
    def release_date(self, new_release_date):
        if not isinstance(new_release_date, str):
            raise ValueError
        else:
            try:
                datetime.strftime(new_release_date, '%b %d, %Y')
                self.__game_release_date = new_release_date
            except:
                raise ValueError

    @property
    def description(self) -> str:
        return self.__game_description

    @description.setter
    def description(self, new_description):
        if (not isinstance(new_description, str)) or new_description == "":
            self.__game_description = None
        else:
            self.__game_description = new_description

    @property
    def publisher(self) -> Publisher:
        return self.__game_publisher

    @publisher.setter
    def publisher(self, new_publisher):
        if not isinstance(new_publisher, Publisher):
            self.__game_publisher = None
        else:
            self.__game_publisher = new_publisher

    @property
    def image_url(self) -> str:
        return self.__game_image_url

    @image_url.setter
    def image_url(self, new_image_url):
        if (not isinstance(new_image_url, str)) or new_image_url == "":
            self.__game_image_url = None
        else:
            self.__game_image_url = new_image_url

    @property
    def website_url(self) -> str:
        return self.__game_website_url

    @website_url.setter
    def website_url(self, new_website_url):
        if (not isinstance(new_website_url, str)) or new_website_url == "":
            self.__game_website_url = None
        else:
            self.__game_website_url = new_website_url

    def __repr__(self):
        return f"<Game {self.__game_id}, {self.__game_title}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return self.__game_id == other.__game_id

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.__game_id < other.__game_id

    def __hash__(self):
        return hash(self.__game_id)

    def add_genre(self, new_genre):
        if isinstance(new_genre, Genre) and not (new_genre in self.__game_genres):
            self.__game_genres.append(new_genre)

    def remove_genre(self, genre_to_remove):
        if isinstance(genre_to_remove, Genre) and genre_to_remove in self.__game_genres:
            self.__game_genres.remove(genre_to_remove)


class User:
    # TODO
    pass


class Review:
    # TODO
    pass


class Wishlist:
    # TODO
    pass
