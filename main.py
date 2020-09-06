import csv
from display import *
from time_converter import *
from menu import MENU

TITLE_INDEX = 0
ALBUM_INDEX = 1
YEAR_INDEX = 2
GENRE_INDEX = 3
TIME_INDEX = 4


def menu(ALBUMS):
    print("MENU")
    print_dictionary(MENU)
 
    option = input("Provide operation number: ")
    while not option in MENU.keys():
        option = input("Provide operation number: ")

    if option == "1":
        ALBUMS = import_albums()
    elif option == "2":
        display_albums(ALBUMS)
    elif option == "3":
        genre = input("Provide genre: ")
        display_albums(get_albums_by(GENRE_INDEX, genre, ALBUMS))
    elif option == "4":
        year = input("Provide year: ")
        display_albums(get_albums_by(YEAR_INDEX, year, ALBUMS))
    elif option == "5":
        display_albums(get_youngest_album(ALBUMS))
    elif option == "6":
        display_albums(sort_albums_by_year(ALBUMS))
    elif option == "7":
        time_from = input("Provide time from: (mm:ss)")
        time_to = input("Provide time to: (mm:ss)")

        display_albums(get_albums_by_time_range(time_from, time_to, ALBUMS))
    else:
        exit()


def import_albums(filepath="text_albums_data.txt"):
    albums = []

    with open(filepath, newline='') as file:
        for row in csv.reader(file):
            albums.append(row)

    return albums


def get_albums_by(column_index, value, ALBUMS):
    selected_albums = []
    value = value.lower()

    for row in ALBUMS:
        if row[column_index].lower() == value:
            selected_albums.append(row)

    return selected_albums


def get_albums_by_time_range(time_from, time_to, ALBUMS):
    # TODO check if time_to is greater than time_from

    time_from = convert_to_seconds(time_from)
    time_to = convert_to_seconds(time_to)
    result = []

    for row in ALBUMS:
        time = row[TIME_INDEX]
        time = convert_to_seconds(time)

        if time_from < time < time_to:
            result.append(row)

    return result


def get_youngest_album(ALBUMS):
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

def get_oldest_album(ALBUMS):
    print("OLDEST ALBUM")
    

def sort_albums_by_year(ALBUMS):
    result = []
    temporary_album_list = ALBUMS

    for row in temporary_album_list:
        row[YEAR_INDEX] = int(row[YEAR_INDEX])

    result = sorted(temporary_album_list, key=lambda row: row[YEAR_INDEX])
    return result


def main():
    ALBUMS = import_albums()
    while True:
        menu(ALBUMS)


main()