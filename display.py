def display_albums(albums):
    for row in albums:
        for column in row:
            print(column, end=" ")
        print()
    print()