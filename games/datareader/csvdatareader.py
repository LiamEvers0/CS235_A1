import os
import csv


class GameFileCSVReader:

    def __init__(self, filename):
        self.__filename = filename
        self.__dataset_of_games = []
        self.__dataset_of_publishers = set()
        self.__dataset_of_genres = set()

    @property
    def dataset_of_games(self) -> list:
        return self.__dataset_of_games

    @property
    def dataset_of_publishers(self) -> set:
        return self.__dataset_of_publishers

    @property
    def dataset_of_genres(self) -> set:
        return self.__dataset_of_genres

    def read_csv_file(self):
        with open(self.__filename, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.__dataset_of_games.append(row)
                self.__dataset_of_publishers.add(row['Publishers'])
                genres = row['Genres'].split(',')
                for genre in genres:
                    self.__dataset_of_genres.add(genre.strip())