for row in range(10):
    for col in range(21):
        if (row == 0 and (col >=0 and col < 12))or\
            (row == 1 and (col == 0 or col == 12)) or\
            (row == 2 and (col == 0 or col == 13)) or\
            (row == 3 and (col == 0 or col > 13)) or\
            (row == 4 and (col == 0 or col == 20)) or\
            (row == 5 and (col == 0 or col == 20)) or\
            (row == 6 and (col >=0 and col < 21))or\
            (row == 7 and (col == 2 or col == 4 or col == 6 or col == 8 or col == 11 or col == 13 or col == 15 or col == 17))or\
            (row == 8 and (col == 3 or col == 7 or col == 12 or col == 16 )):
            print("*", end= ' ')
        else:
            print(" ", end= ' ')
    print()