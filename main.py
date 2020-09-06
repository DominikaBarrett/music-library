import csv
from display import *

ALBUMS = []
TITLE_INDEX = 0
ALBUM_INDEX = 1
YEAR_INDEX = 2
GENRE_INDEX = 3
TIME_INDEX = 4


def menu():
    global ALBUMS
    print("MENU")
    print("1. IMPORT ALBUMS")
    print("2. DISPLAY ALBUMS")
    print("3. GET ALBUMS BY GENRE")
    print("4. GET ALBUMS BY YEAR")
    print("5. GET YOUNGEST ALBUMS")
    print("6. SORT ALBUMS BY YEAR")
    print("X. EXIT")

    option = input("Provide operation number: ")

    if option == "1":
        ALBUMS = import_albums()
    elif option == "2":
        display_albums(ALBUMS)
    elif option == "3":
        genre = input("Provide genre: ")
        display_albums(get_albums_by(GENRE_INDEX, genre))
    elif option == "4":
        year = input("Provide year: ")
        display_albums(get_albums_by(YEAR_INDEX, year))
    elif option == "5":
        display_albums(get_youngest_album())
    elif option == "6":
        display_albums(sort_albums_by_year())
    else:
        exit()


def import_albums(filepath="text_albums_data.txt"):
    albums = []

    with open(filepath, newline='') as file:
        for row in csv.reader(file):
            albums.append(row)

    return albums


def get_albums_by(column_index, value):
    selected_albums = []
    value = value.lower()

    for row in ALBUMS:
        if row[column_index].lower() == value:
            selected_albums.append(row)

    return selected_albums


def get_albums_by_time_range(time_range_from, time_range_to):
    pass


def get_youngest_album():
    result = []
    years = []

    for row in ALBUMS:
        years.append(int(row[YEAR_INDEX]))

    max_years = []
    max_year = max(years)

    for index, element in enumerate(years):
        if max_year == element:
            max_years.append(index)

    for element in max_years:
        result.append(ALBUMS[element])

    return result


def sort_albums_by_year():
    result = []
    temporary_album_list = ALBUMS

    for row in temporary_album_list:
        row[YEAR_INDEX] = int(row[YEAR_INDEX])

    result = sorted(temporary_album_list, key=lambda row: row[YEAR_INDEX])
    return result


def main():
    global ALBUMS
    ALBUMS = import_albums()
    while True:
        menu()


main()
