def display_albums(albums):
    for index, row in enumerate(albums,1):
        print(f'|{index:2}|', end="")
        for column in row:
            print(f' {column:15}|', end="")
        print()
    print()

def print_dictionary(dictionary):
    for key in dictionary.keys():
        print(f'{key}. {dictionary[key]}')

def print_headers():
    pass