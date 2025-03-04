for row in range(15):
    for col in range (15):
        if (row == 0 and (col > 4 and col <10 ))or\
            (row == 1 and (col == 4 or col == 10))or\
            (row == 2 and (col > 3 or col < 11))or\
            (row == 2 and (col < 3 or col > 11))or\
            (row == 3 and (col < 4 or col > 10))or\
            (row == 4 and (col > 3 or col < 10))or\
            (row == 5 and (col == 3 or col == 11))or\
            (row == 5 and (col == 5 or col == 13))or\
            (row == 6 and (col == 4 or col == 12)):
            print('*', end= ' ') 
        else:
            print(' ', end= ' ')
    print()