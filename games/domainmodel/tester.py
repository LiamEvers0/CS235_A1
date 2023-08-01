from games.datareader.csvdatareader import GameFileCSVReader
from games.domainmodel.model import Game, Genre, Publisher


def main():
    csvdatareader1 = GameFileCSVReader(
        'C:Users\liame\PycharmProjects\CS235_2023_GamesWebApp_Assignment1_CodeSkeleton\games\data\games.csv')

    games = csvdatareader1.read_csv_file()
    for game in games:
        print(game)


main()
