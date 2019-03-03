import time


def clear_my_screen():
    print " \n" * 40


class Item(object):
    def __init__(self, number, free, l1):
        list = []
        self.number = number
        self.free = free
        self.temp_numbers = list

    def set_number(self, number):
        self.number = number

    def print_number(self):
        print "%s" % (self.number)

    def init_temp_numbers(self):
        self.temp_numbers = []
        return self.temp_numbers

    def add_new_number(self, num):
        self.temp_numbers.append(num)


def print_board(board):
    print "   |   | " + "    " + "   |   | " + "    " + "   |   | "
    print ' ' + str(board[0][0]) + ' | ' + str(board[0][1]) + ' | ' + str(board[0][2]) + '    ' + str(
        board[0][3]) + ' | ' + str(board[0][4]) + ' | ' + str(board[0][5]) + '    ' + str(board[0][6]) + ' | ' + str(
        board[0][7]) + ' | ' + str(board[0][8])
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print '------------------------------------'
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print ' ' + str(board[1][0]) + ' | ' + str(board[1][1]) + ' | ' + str(board[1][2]) + '    ' + str(
        board[1][3]) + ' | ' + str(board[1][
                                       4]) + ' | ' + str(board[1][5]) + '    ' + str(board[1][6]) + ' | ' + str(
        board[1][7]) + ' | ' + str(board[1][8])
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print '------------------------------------'
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print ' ' + str(board[2][0]) + ' | ' + str(board[2][1]) + ' | ' + str(board[2][2]) + '    ' + str(
        board[2][3]) + ' | ' + str(board[2][
                                       4]) + ' | ' + str(board[2][5]) + '    ' + str(board[2][6]) + ' | ' + str(
        board[2][7]) + ' | ' + str(board[2][8])
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print '------------------------------------'
    print "\n"
    print "   |   | " + "    " + "   |   | " + "    " + "   |   | "
    print ' ' + str(board[3][0]) + ' | ' + str(board[3][1]) + ' | ' + str(board[3][2]) + '    ' + str(
        board[3][3]) + ' | ' + str(board[3][
                                       4]) + ' | ' + str(board[3][5]) + '    ' + str(board[3][6]) + ' | ' + str(
        board[3][7]) + ' | ' + str(board[3][8])
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print '------------------------------------'
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print ' ' + str(board[4][0]) + ' | ' + str(board[4][1]) + ' | ' + str(board[4][2]) + '    ' + str(
        board[4][3]) + ' | ' + str(board[4][
                                       4]) + ' | ' + str(board[4][5]) + '    ' + str(board[4][6]) + ' | ' + str(
        board[4][7]) + ' | ' + str(board[4][8])
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print '------------------------------------'
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print ' ' + str(board[5][0]) + ' | ' + str(board[5][1]) + ' | ' + str(board[5][2]) + '    ' + str(
        board[5][3]) + ' | ' + str(board[5][
                                       4]) + ' | ' + str(board[5][5]) + '    ' + str(board[5][6]) + ' | ' + str(
        board[5][7]) + ' | ' + str(board[5][8])
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print '------------------------------------'
    print "\n"
    print "   |   | " + "    " + "   |   | " + "    " + "   |   | "
    print ' ' + str(board[6][0]) + ' | ' + str(board[6][1]) + ' | ' + str(board[6][2]) + '    ' + str(
        board[6][3]) + ' | ' + str(board[6][
                                       4]) + ' | ' + str(board[6][5]) + '    ' + str(board[6][6]) + ' | ' + str(
        board[6][7]) + ' | ' + str(board[6][8])
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print '------------------------------------'
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print ' ' + str(board[7][0]) + ' | ' + str(board[7][1]) + ' | ' + str(board[7][2]) + '    ' + str(
        board[7][3]) + ' | ' + str(board[7][
                                       4]) + ' | ' + str(board[7][5]) + '    ' + str(board[7][6]) + ' | ' + str(
        board[7][7]) + ' | ' + str(board[7][8])
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print '------------------------------------'
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print ' ' + str(board[8][0]) + ' | ' + str(board[8][1]) + ' | ' + str(board[8][2]) + '    ' + str(
        board[8][3]) + ' | ' + str(board[8][
                                       4]) + ' | ' + str(board[8][5]) + '    ' + str(board[8][6]) + ' | ' + str(
        board[8][7]) + ' | ' + str(board[8][8])
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print '------------------------------------'
    print "\n"


def sudo_style_print(board):
    print '-------------------------------------'
    print "   |   | " + "    " + "   |   | " + "    " + "   |   | "
    print ' ' + str(board[0][0].number) + ' | ' + str(board[0][1].number) + ' | ' + str(
        board[0][2].number) + '    ' + str(
        board[0][3].number) + ' | ' + str(board[0][4].number) + ' | ' + str(board[0][5].number) + '    ' + str(
        board[0][6].number) + ' | ' + str(
        board[0][7].number) + ' | ' + str(board[0][8].number)
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print '----------   ----------    ----------'
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print ' ' + str(board[1][0].number) + ' | ' + str(board[1][1].number) + ' | ' + str(
        board[1][2].number) + '    ' + str(
        board[1][3].number) + ' | ' + str(board[1][
                                              4].number) + ' | ' + str(board[1][5].number) + '    ' + str(
        board[1][6].number) + ' | ' + str(
        board[1][7].number) + ' | ' + str(board[1][8].number)
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print '----------   ----------    ----------'
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print ' ' + str(board[2][0].number) + ' | ' + str(board[2][1].number) + ' | ' + str(
        board[2][2].number) + '    ' + str(
        board[2][3].number) + ' | ' + str(board[2][
                                              4].number) + ' | ' + str(board[2][5].number) + '    ' + str(
        board[2][6].number) + ' | ' + str(
        board[2][7].number) + ' | ' + str(board[2][8].number)
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print '-------------------------------------'
    print "   |   | " + "    " + "   |   | " + "    " + "   |   | "
    print ' ' + str(board[3][0].number) + ' | ' + str(board[3][1].number) + ' | ' + str(
        board[3][2].number) + '    ' + str(
        board[3][3].number) + ' | ' + str(board[3][
                                              4].number) + ' | ' + str(board[3][5].number) + '    ' + str(
        board[3][6].number) + ' | ' + str(
        board[3][7].number) + ' | ' + str(board[3][8].number)
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print '----------   ----------    ----------'
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print ' ' + str(board[4][0].number) + ' | ' + str(board[4][1].number) + ' | ' + str(
        board[4][2].number) + '    ' + str(
        board[4][3].number) + ' | ' + str(board[4][
                                              4].number) + ' | ' + str(board[4][5].number) + '    ' + str(
        board[4][6].number) + ' | ' + str(
        board[4][7].number) + ' | ' + str(board[4][8].number)
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print '----------   ----------    ----------'
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print ' ' + str(board[5][0].number) + ' | ' + str(board[5][1].number) + ' | ' + str(
        board[5][2].number) + '    ' + str(
        board[5][3].number) + ' | ' + str(board[5][
                                              4].number) + ' | ' + str(board[5][5].number) + '    ' + str(
        board[5][6].number) + ' | ' + str(
        board[5][7].number) + ' | ' + str(board[5][8].number)
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print '-------------------------------------'
    print "   |   | " + "    " + "   |   | " + "    " + "   |   | "
    print ' ' + str(board[6][0].number) + ' | ' + str(board[6][1].number) + ' | ' + str(
        board[6][2].number) + '    ' + str(
        board[6][3].number) + ' | ' + str(board[6][
                                              4].number) + ' | ' + str(board[6][5].number) + '    ' + str(
        board[6][6].number) + ' | ' + str(
        board[6][7].number) + ' | ' + str(board[6][8].number)
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print '----------   ----------    ----------'
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print ' ' + str(board[7][0].number) + ' | ' + str(board[7][1].number) + ' | ' + str(
        board[7][2].number) + '    ' + str(
        board[7][3].number) + ' | ' + str(board[7][
                                              4].number) + ' | ' + str(board[7][5].number) + '    ' + str(
        board[7][6].number) + ' | ' + str(
        board[7][7].number) + ' | ' + str(board[7][8].number)
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print '----------   ----------    ----------'
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print ' ' + str(board[8][0].number) + ' | ' + str(board[8][1].number) + ' | ' + str(
        board[8][2].number) + '    ' + str(
        board[8][3].number) + ' | ' + str(board[8][
                                              4].number) + ' | ' + str(board[8][5].number) + '    ' + str(
        board[8][6].number) + ' | ' + str(
        board[8][7].number) + ' | ' + str(board[8][8].number)
    print "   |   | " + "    " + "   |   | " + "       |   |  "
    print '-------------------------------------'
    print "\n"


def number_matrix_print(board):
    for i in range(9):
        for j in range(9):
            print board[i][j].number,
        print "\n"


def build_sudoku_board_generator(num):

    if num == 1:
        board = [[0, 0, 0, 1, 0, 5, 0, 6, 8],
                 [0, 0, 0, 0, 0, 0, 7, 0, 1],
                 [9, 0, 1, 0, 0, 0, 0, 3, 0],
                 [0, 0, 7, 0, 2, 6, 0, 0, 0],
                 [5, 0, 0, 0, 0, 0, 0, 0, 3],
                 [0, 0, 0, 8, 7, 0, 4, 0, 0],
                 [0, 3, 0, 0, 0, 0, 8, 0, 5],
                 [1, 0, 5, 0, 0, 0, 0, 0, 0],
                 [7, 9, 0, 4, 0, 1, 0, 0, 0]]
    elif num == 2:
        board = [[0, 2, 0, 6, 0, 8, 0, 0, 0],
                 [5, 8, 0, 0, 0, 9, 7, 0, 0],
                 [0, 0, 0, 0, 4, 0, 0, 0, 0],
                 [3, 7, 0, 0, 0, 0, 5, 0, 0],
                 [6, 0, 0, 0, 0, 0, 0, 0, 4],
                 [0, 0, 8, 0, 0, 0, 0, 1, 3],
                 [0, 0, 0, 0, 2, 0, 0, 0, 0],
                 [0, 0, 9, 8, 0, 0, 0, 3, 6],
                 [0, 0, 0, 3, 0, 6, 0, 9, 0]]
    elif num == 3:
        board = [[1, 0, 0, 4, 8, 9, 0, 0, 6],
                 [7, 3, 0, 0, 0, 0, 0, 4, 0],
                 [0, 0, 0, 0, 0, 1, 2, 9, 5],
                 [0, 0, 7, 1, 2, 0, 6, 0, 0],
                 [5, 0, 0, 7, 0, 3, 0, 0, 8],
                 [0, 0, 6, 0, 9, 5, 7, 0, 0],
                 [9, 1, 4, 6, 0, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0, 0, 3, 7],
                 [8, 0, 0, 5, 1, 2, 0, 0, 4]]
    elif num == 4:
        board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                 [6, 0, 0, 1, 9, 5, 0, 0, 0],
                 [0, 9, 8, 0, 0, 0, 0, 6, 0],
                 [8, 0, 0, 0, 6, 0, 0, 0, 3],
                 [4, 0, 0, 8, 0, 3, 0, 0, 1],
                 [7, 0, 0, 0, 2, 0, 0, 0, 6],
                 [0, 6, 0, 0, 0, 0, 2, 8, 0],
                 [0, 0, 0, 4, 1, 9, 0, 0, 5],
                 [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    elif num == 5:
        board = [[0, 0, 0, 4, 0, 0, 2, 0, 0],
                 [0, 0, 2, 0, 0, 0, 0, 1, 8],
                 [5, 0, 6, 9, 0, 0, 0, 3, 0],
                 [0, 6, 9, 0, 0, 0, 3, 0, 0],
                 [0, 5, 0, 0, 0, 0, 0, 2, 1],
                 [8, 0, 0, 1, 5, 7, 6, 0, 9],
                 [0, 0, 0, 0, 3, 0, 9, 6, 0],
                 [9, 0, 0, 6, 0, 2, 0, 5, 0],
                 [0, 0, 0, 0, 0, 0, 7, 0, 2]]
    elif num == 6:
        # Difficult board
        board = [[0, 0, 0, 6, 0, 0, 4, 0, 0],
                 [7, 0, 0, 0, 0, 3, 6, 0, 0],
                 [0, 0, 0, 0, 9, 1, 0, 8, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 5, 0, 1, 8, 0, 0, 0, 3],
                 [0, 0, 0, 3, 0, 6, 0, 4, 5],
                 [0, 4, 0, 2, 0, 0, 0, 6, 0],
                 [9, 0, 3, 0, 0, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0, 1, 0, 0]]

    return board


def init_sudoku_board(original_input):
    #bb = [[Item] * 9] * 9
    new_board = [[Item] * 9, [Item] * 9, [Item] * 9, [Item] * 9, [Item] * 9, [Item] * 9, [Item] * 9, [Item] * 9, [Item] * 9]


    # Init temp list of number for each item
    list = []

    for i in range(9):
        for j in range(9):
            if original_input[i][j] == 0:
                # 1 if its free cell with 0 value.
                new_board[i][j] = Item(original_input[i][j], 1, list)
            else:
                new_board[i][j] = Item(original_input[i][j], 0, list)

    number_matrix_print(new_board)

    #sudo_style_print(new_board)

    return new_board


def regular_matrix_print(sar):
 for i in range(9):
     for j in range(9):
         print sar[i][j]


def check_my_box(board, number, row, row2, col, col2):

    for i in range(row, row2):
        for j in range(col, col2):
            if board[i][j].number == number:
                return True
    return False


def box_numbers_valid_print(board, row, row2, col, col2):

    for i in range(row, row2):
        for j in range(col, col2):
            for x in range(len(board[i][j].temp_numbers)):
                if board[i][j].free == 1:
                    print "{},{} ---> {}".format(i, j, board[i][j].temp_numbers[x])


def two_numbers_in_temp_check(board, row, row2, col, col2):

    # Function check if there are 2 cells with only 2 numbers in their temp array,
    # add their place of the cells to place_of_cell list and the numbers in their temp into list_of_two list.
    # Example cell 1,3 [1,2]  cell 1,4 [1,3] --> result : cell 1 = 2 cell 2 = 3

    list_of_two = []
    place_of_cell = []
    count_of_two = 0
    for i in range(row, row2):
        for j in range(col, col2):
            if len(board[i][j].temp_numbers) == 2 and board[i][j].free == 1:
                count_of_two += 1
                place_of_cell.append(i)
                place_of_cell.append(j)
                for x in range(len(board[i][j].temp_numbers)):
                    list_of_two.append(board[i][j].temp_numbers[x])

    flag = 0
    # TODO: need to check if can be deleted.
    for i in range(len(list_of_two)):
        if list_of_two.count(list_of_two[i]) == 1:
            flag = 1

    if count_of_two == 2 and flag == 1:
        board[place_of_cell[0]][place_of_cell[1]].set_number(list_of_two[1])
        board[place_of_cell[0]][place_of_cell[1]].free = 0
        board[place_of_cell[2]][place_of_cell[3]].set_number(list_of_two[3])
        board[place_of_cell[2]][place_of_cell[3]].free = 0
        return True
    return False


def find_two_and_mark(board, row, col):

    if check_num_area_box_location(row, col) == 4:
        two_numbers_in_temp_check(board, 3, 6, 0, 3)
    if check_num_area_box_location(row, col) == 5:
        two_numbers_in_temp_check(board, 3, 6, 3, 6)

    if check_num_area_box_location(row, col) == 5:
        two_numbers_in_temp_check(board, 3, 6, 3, 9)


def print_num_valid_options_per_box(board, row, col):

    if check_num_area_box_location(row, col) == 1:
        box_numbers_valid_print(board, 0, 3, 0, 3)

    if check_num_area_box_location(row, col) == 2:
        box_numbers_valid_print(board, 0, 3, 3, 6)

    if check_num_area_box_location(row, col) == 3:
        box_numbers_valid_print(board, 0, 3, 6, 9)

    if check_num_area_box_location(row, col) == 4:
        box_numbers_valid_print(board, 3, 6, 0, 3)

    if check_num_area_box_location(row, col) == 5:
        box_numbers_valid_print(board, 3, 6, 3, 6)

    if check_num_area_box_location(row, col) == 6:
        box_numbers_valid_print(board, 3, 6, 6, 9)

    if check_num_area_box_location(row, col) == 7:
        box_numbers_valid_print(board, 6, 9, 0, 3)

    if check_num_area_box_location(row, col) == 8:
        box_numbers_valid_print(board, 6, 9, 3, 6)

    if check_num_area_box_location(row, col) == 9:
        box_numbers_valid_print(board, 6, 9, 6, 9)


def col_numbers_valid_print(board, col):

    list = []
    print "col valid :",col
    for row_number in range(9):
        if board[row_number][col].free == 0:
          list.append(board[row_number][col].number)
    for num in range(1,10):
      if num  not in list:
         print num,
    print "\n"


def col_numbers_valid_check(board, col):

    list_exist = []
    check_valid = []
    new_valid = []
    place = []

    for row_number in range(9):
        if board[row_number][col].free == 0:
            list_exist.append(board[row_number][col].number)
    for num in range(1, 10):
          if list_exist.count(num) == 0:
              check_valid.append(num)

    # print "option num"
    # for i in range(len(check_valid)):
    #     print check_valid[i]
    print "\n"


    for row_number in range(9):
       if board[row_number][col].free == 1:
        for i in range(len(check_valid)):
            if check_my_row(board, check_valid[i], row_number) is False and check_my_col(board, check_valid[i],
                                                                                  col) is False and check_num_existence_in_area_box(
                    board, check_valid[i], row_number, col) is False:
             new_valid.append(num)
             place.append(check_valid[i])
             place.append(row_number)

    if len(new_valid) > 0:
      print "col:",col
      for i in range(len(place)):
          print place[i],
    # x = len(place)
    # if len(place) > 0:
    #     print "col:", col
    #     for i in range(len(place)-1):
    #         print "num {} in cell {}".format(place[i], place[i+1])
    #
    #         # if i % 2 == 0 and i is not 0:
    #         #     print "\n"


def row_numbers_valid_check(board, row):

    list_exist = []
    check_valid = []
    new_valid = []
    place = []

    for col_number in range(9):
        if board[row][col_number].free == 0:
            list_exist.append(board[row][col_number].number)
    for num in range(1, 10):
          if list_exist.count(num) == 0:
              check_valid.append(num)

    # print "option num"
    # for i in range(len(check_valid)):
    #     print "a",check_valid[i]
    if len(check_valid) > 0:
      print "\n"


    for col_number in range(9):
       if board[row][col_number].free == 1:
        for i in range(len(check_valid)):
            if check_my_row(board, check_valid[i], row) is False and check_my_col(board, check_valid[i],
                                                                                  col_number) is False and check_num_existence_in_area_box(
                    board, check_valid[i], row, col_number) is False:
             new_valid.append(num)
             place.append(check_valid[i])
             place.append(col_number)

    # if len(new_valid) > 0:
    #   for i in range(len(new_valid)):
    #       print new_valid[i]
    x = len(place)
    if len(place) > 0:
        print "row:", row
        for i in range(len(place)):
            print place[i],

    print "\n"
    #New list printing check:
    num_list = []
    if len(place) > 0:
        for i in range(len(place)):
            if i % 2 == 0:
             num_list.append(place[i])

    num_set = list(set(num_list))
    for i in range(len(num_set)):
        print num_set[i],


def check_my_row(board, number, row):

    for col_number in range(9):
        if board[row][col_number].number == number:
            return True
    return False


def check_my_col(board, number, col):

    for row_number in range(9):
        if board[row_number][col].number == number:
            return True
    return False


def check_num_area_box_location(number_row, number_col):

    # Box 1 area
    if (number_row == 0 or number_row == 1 or number_row == 2) and number_col < 3:
        #print "1"
        return 1

    # Box 2 area
    if (number_row == 0 or number_row == 1 or number_row == 2) and number_col > 2 and number_col < 6:
        #print "2"
        return 2

    # Box 3 area
    if (number_row == 0 or number_row == 1 or number_row == 2) and number_col >= 6 and number_col < 9:
        #print "3"
        return 3

    # Box 4 area
    if (number_row == 3 or number_row == 4 or number_row == 5) and number_col < 3:
        #print "4"
        return 4

    # Box 5 area
    if (number_row == 3 or number_row == 4 or number_row == 5) and number_col > 2 and number_col < 6:
        #print "5"
        return 5

    # Box 6 area
    if (number_row == 3 or number_row == 4 or number_row == 5) and number_col >= 6 and number_col < 9:
        #print "6"
        return 6

    # Box 7 area
    if (number_row == 6 or number_row == 7 or number_row == 8) and number_col < 3:
        #print "7"
        return 7

    # Box 8 area
    if (number_row == 6 or number_row == 7 or number_row == 8) and number_col > 2 and number_col < 6:
       #print "8"
       return 8

    # Box 9 area
    if (number_row == 6 or number_row == 7 or number_row == 8) and number_col >= 6 and number_col < 9:
       #print "9"
       return 9


def check_num_existence_in_area_box(board, num, row, col):

    if check_num_area_box_location(row, col) == 1:
        if check_my_box(board, num, 0, 3, 0, 3) is False:
            return False
    if check_num_area_box_location(row, col) == 2:
        if check_my_box(board, num, 0, 3, 3, 6) is False:
            return False
    if check_num_area_box_location(row, col) == 3:
        if check_my_box(board, num, 0, 3, 6, 9) is False:
            return False

    if check_num_area_box_location(row, col) == 4:
        if check_my_box(board, num, 3, 6, 0, 3) is False:
            return False
    if check_num_area_box_location(row, col) == 5:
        if check_my_box(board, num, 3, 6, 3, 6) is False:
            return False
    if check_num_area_box_location(row, col) == 6:
        if check_my_box(board, num, 3, 6, 6, 9) is False:
            return False

    if check_num_area_box_location(row, col) == 7:
        if check_my_box(board, num, 6, 9, 0, 3) is False:
            return False
    if check_num_area_box_location(row, col) == 8:
        if check_my_box(board, num, 6, 9, 3, 6) is False:
            return False
    if check_num_area_box_location(row, col) == 9:
        if check_my_box(board, num, 6, 9, 6, 9) is False:
            return False


    return True


def concatenate_and_merge_temp_list(board, row, row2, col, col2):

    new_list = []
    for i in range(row, row2):
        for j in range(col, col2):
            if board[i][j].free == 1:
                new_list += board[i][j].temp_numbers

    new_list.sort()
    for i in range(len(new_list)):
        print new_list[i],

    print "\n"
    sort_list = list(set(new_list))
    for i in range(len(sort_list)):
        print sort_list[i],

    print "\n"
   # for i in range(len(new_list)):
    for j in range(len(sort_list)):
         print new_list.count(sort_list[j]),

    for j in range(len(sort_list)):
        if new_list.count(sort_list[j]) == 1:
            print "only one " + str(sort_list[j])


def one_number_place_return(board, row, row2, col, col2):

    # ******  Function purpose ******
    # Scan all the free cells in specific box, and add their temp number into new_list (all the temp of all cells)
    # we do sort to the array and find number which appear only 1 time, if there is number like that the function return the number
    # Example: 111122234444 --> 1 = 4 time 2 = 3 time 3 = 1 time 4 = 4 time so function return number 3

    count_of_ones = 0
    new_list = []
    for i in range(row, row2):
        for j in range(col, col2):
            if board[i][j].free == 1:
             new_list += board[i][j].temp_numbers

    new_list.sort()
    sort_list = list(set(new_list))

    for j in range(len(sort_list)):
        if new_list.count(sort_list[j]) == 1:
            count_of_ones += 1
            return sort_list[j]
    return 0


def concatenate_num_valid_options_per_box(board, row, col):

    if check_num_area_box_location(row, col) == 1:
        concatenate_and_merge_temp_list(board, 0, 3, 0, 3)

    if check_num_area_box_location(row, col) == 2:
        concatenate_and_merge_temp_list(board, 0, 3, 3, 6)

    if check_num_area_box_location(row, col) == 3:
        concatenate_and_merge_temp_list(board, 0, 3, 6, 3)

    if check_num_area_box_location(row, col) == 4:
        concatenate_and_merge_temp_list(board, 3, 6, 0, 3)

    if check_num_area_box_location(row, col) == 5:
        concatenate_and_merge_temp_list(board, 3, 6, 3, 6)

    if check_num_area_box_location(row, col) == 6:
        concatenate_and_merge_temp_list(board, 3, 6, 6, 9)

    if check_num_area_box_location(row, col) == 7:
        concatenate_and_merge_temp_list(board, 6, 9, 0, 3)

    if check_num_area_box_location(row, col) == 8:
        concatenate_and_merge_temp_list(board, 6, 9, 3, 6)

    if check_num_area_box_location(row, col) == 9:
        concatenate_and_merge_temp_list(board, 6, 9, 6, 9)


def number_option_print(board, row, col):

    # if row and col == 10 print all board option.else, print specific number

    if row == 10 and col == 10:
        for i in range(9):
            for j in range(9):
                for x in range(len(board[i][j].temp_numbers)):
                    if len(board[i][j].temp_numbers) > 1 and board[i][j].free == 1:
                      print "{},{} ---> {}".format(i, j, board[i][j].temp_numbers[x])
                    if x == len(board[i][j].temp_numbers) - 1:
                        print "\n"
    else:
        for x in range(len(board[row][col].temp_numbers)):
            print board[row][col].temp_numbers[x],


def finish_game_check(board):

    for i in range(9):
            for j in range(9):
                if board[i][j].free == 1:
                    return False
    return True


def only_one_option_print(board):
    for i in range(9):
        for j in range(9):
            if len(board[i][j].temp_numbers) == 1:
               # if board[i][j].free == 1:
                 print "Row {} Col {} --> {}".format(i, j, board[i][j].temp_numbers[0])
                #print board[i][j].temp_numbers[0],


def find_cell_place_with_two_num(board):

    if two_numbers_in_temp_check(board, 0, 3, 0, 3) is True:
        flush_temp_number_list(board)
        update_temp_option_per_cell(board)
        return True
    if two_numbers_in_temp_check(board, 0, 3, 3, 6) is True:
        flush_temp_number_list(board)
        update_temp_option_per_cell(board)
        return True
    if two_numbers_in_temp_check(board, 0, 3, 6, 9) is True:
        flush_temp_number_list(board)
        update_temp_option_per_cell(board)
        return True
    if two_numbers_in_temp_check(board, 3, 6, 0, 3) is True:
        flush_temp_number_list(board)
        update_temp_option_per_cell(board)
        return True
    if two_numbers_in_temp_check(board, 3, 6, 3, 6) is True:
        flush_temp_number_list(board)
        update_temp_option_per_cell(board)
        return True
    if two_numbers_in_temp_check(board, 3, 6, 6, 9) is True:
        flush_temp_number_list(board)
        update_temp_option_per_cell(board)
        return True
    if two_numbers_in_temp_check(board, 6, 9, 0, 3) is True:
        flush_temp_number_list(board)
        update_temp_option_per_cell(board)
        return True
    if two_numbers_in_temp_check(board, 6, 9, 3, 6) is True:
        flush_temp_number_list(board)
        update_temp_option_per_cell(board)
        return True
    if two_numbers_in_temp_check(board, 6, 9, 6, 9) is True:
        flush_temp_number_list(board)
        update_temp_option_per_cell(board)
        return True
    return False


def find_cell_place_by_number(board):

    # ******  Function purpose ******
    # checking the whole box and find number which is in free cell, and appear only one time in the whole temp array number
    # of the specific Box, IF there is cell which have only one number appear in his temp array and other cells doesnt have it,
    # we add this number to the board and set free = 0
    # The function runs on all over the boxes.

    x = one_number_place_return(board, 0, 3, 0, 3)
    if x != 0:
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j].free == 1:
                    for k in range(len(board[i][j].temp_numbers)):
                     if board[i][j].temp_numbers == x:
                        board[i][j].set_number(x)
                        board[i][j].free = 0
                        return True

    x = one_number_place_return(board, 0, 3, 3, 6)
    if x != 0:
        for i in range(0, 3):
            for j in range(3, 6):
                if board[i][j].free == 1:
                    for k in range(len(board[i][j].temp_numbers)):
                     if board[i][j].temp_numbers == x:
                        board[i][j].set_number(x)
                        board[i][j].free = 0
                        return True

    x = one_number_place_return(board, 0, 3, 6, 9)
    if x != 0:
        for i in range(0, 3):
            for j in range(6, 9):
                if board[i][j].free == 1:
                    for k in range(len(board[i][j].temp_numbers)):
                      if board[i][j].temp_numbers[k] == x:
                         board[i][j].set_number(x)
                         board[i][j].free = 0
                         return True

    x = one_number_place_return(board, 3, 6, 0, 3)
    if x != 0:
        for i in range(3, 6):
            for j in range(0, 3):
                if board[i][j].free == 1:
                    for k in range(len(board[i][j].temp_numbers)):
                        if board[i][j].temp_numbers[k] == x:
                            board[i][j].set_number(x)
                            board[i][j].free = 0
                            return True

    x = one_number_place_return(board, 3, 6, 3, 6)
    if x != 0:
        for i in range(3, 6):
            for j in range(3, 6):
                if board[i][j].free == 1:
                    for k in range(len(board[i][j].temp_numbers)):
                        if board[i][j].temp_numbers[k] == x:
                            board[i][j].set_number(x)
                            board[i][j].free = 0
                            return True

    x = one_number_place_return(board, 3, 6, 6, 9)
    if x != 0:
        for i in range(3, 6):
            for j in range(6, 9):
                if board[i][j].free == 1:
                    for k in range(len(board[i][j].temp_numbers)):
                        if board[i][j].temp_numbers[k] == x:
                            board[i][j].set_number(x)
                            board[i][j].free = 0
                            return True

    x = one_number_place_return(board, 6, 9, 0, 3)
    if x != 0:
        for i in range(6, 9):
            for j in range(0, 3):
                if board[i][j].free == 1:
                    for k in range(len(board[i][j].temp_numbers)):
                        if board[i][j].temp_numbers[k] == x:
                            board[i][j].set_number(x)
                            board[i][j].free = 0
                            return True

    x = one_number_place_return(board, 6, 9, 3, 6)
    if x != 0:
        for i in range(6, 9):
            for j in range(3, 9):
                if board[i][j].free == 1:
                    for k in range(len(board[i][j].temp_numbers)):
                        if board[i][j].temp_numbers[k] == x:
                            board[i][j].set_number(x)
                            board[i][j].free = 0
                            return True

    x = one_number_place_return(board, 6, 9, 6, 9)
    if x != 0:
        for i in range(6, 9):
            for j in range(6, 9):
                if board[i][j].free == 1:
                    for k in range(len(board[i][j].temp_numbers)):
                        if board[i][j].temp_numbers[k] == x:
                            board[i][j].set_number(x)
                            board[i][j].free = 0
                            return True
    return False


def flush_temp_number_list(board):
    # clear all the number option array for each cell
    for i in range(9):
        for j in range(9):
            if board[i][j].free == 1:
                board[i][j].temp_numbers = []


def update_temp_option_per_cell(board):


    for i in range(9):
        for j in range(9):
            # If its empty cell we check number validity
            if board[i][j].free == 1:
                #num_of_change += 1
                for num in range(1, 10):
                    if check_my_row(board, num, i) is False and check_my_col(board, num,
                                                                             j) is False and check_num_existence_in_area_box(
                        board, num, i, j) is False:
                        # print i, j
                        board[i][j].add_new_number(num)


def solution_logic(board):
    num_of_steps = 0
    checking_one_number = True
    loop = 1
    one = 0
    num_with_one_option = 1
    while finish_game_check(board) is not True:
        num_of_steps += 1
        # This loop is responsible to find all cells which have only one option valid
        while loop == 1 and num_with_one_option == 1:
            loop = 0
            num_with_one_option = 0
            for i in range(9):
                for j in range(9):
                    # If its empty cell we check number validity
                    if board[i][j].free == 1:
                        # For each number between 1-9 check if it can be valid for each cell on the board
                        for num in range(1, 10):
                            if check_my_row(board, num, i) is False and check_my_col(board, num,
                                                                                     j) is False and check_num_existence_in_area_box(board, num, i, j) is False:

                                board[i][j].add_new_number(num)
                        if len(board[i][j].temp_numbers) == 1:
                            # If there is only one option which is valid for specific cell, change the number
                            board[i][j].free = 0
                            num_with_one_option = 1
                            loop = 1
                            one += 1
                            board[i][j].set_number(board[i][j].temp_numbers[0])
            if num_with_one_option == 1:
                flush_temp_number_list(board)

        loop = 1
        num_with_one_option = 1
        # Running with while loop to check number validity in Box ( if there is only one option for number in box)
        guz = 0

        while checking_one_number and guz == 0:
            checking_one_number = find_cell_place_by_number(board)

        checking_one_number = 1

        if find_cell_place_with_two_num(board):
            continue

        flush_temp_number_list(board)
    print "Sudoku has been solved in {}".format((num_of_steps))

# def solution_logic(board):
#
#     num_of_change = 0
#     checking_one_number = True
#     tot = 0
#     flag = 1
#     one_number_counter = 0
#     one_number_valid = 0
#     #while finish_game_check(board) is not True:
#     while flag == 1:
#         one_number_valid = 1
#         flag = 0
#         for i in range(9):
#             for j in range(9):
#                 # If its empty cell we check number validity
#                 if board[i][j].free == 1:
#                     num_of_change += 1
#                     for num in range(1, 10):
#                       if check_my_row(board, num, i) is False and check_my_col(board, num, j) is False and check_num_existence_in_area_box(board, num, i, j) is False:
#                         # print i, j
#                         board[i][j].add_new_number(num)
#                         # board[i][j].set_number(num)
#                         tot += 1
#                     if len(board[i][j].temp_numbers) == 1:
#                         board[i][j].free = 0
#                         one_number_valid = 0
#                         if one_number_valid == 0: ##  was = 1
#                             flag = 1 ##
#                         one_number_counter += 1
#                         board[i][j].set_number(board[i][j].temp_numbers[0])
#
#        # one_number_valid = checking_one_number(board, one_number_valid)
#         if flag == 1:
#           flush_temp_number_list(board)
#
#         print " done"
#     # Checking if there is one number in the whole box and put it in the cell
#     kaki = 0
#
#     while finish_game_check(board) is not True:
#         while checking_one_number:
#             checking_one_number = find_cell_place_by_number(board)
#
#         flush_temp_number_list(board)
#         # update_temp_option_per_cell(board)
#         for i in range(9):
#             for j in range(9):
#                 # If its empty cell we check number validity
#                 if board[i][j].free == 1:
#                     num_of_change += 1
#                     for num in range(1, 10):
#                         if check_my_row(board, num, i) is False and check_my_col(board, num,
#                                                                                  j) is False and check_num_existence_in_area_box(
#                             board, num, i, j) is False:
#                             # print i, j
#                             board[i][j].add_new_number(num)
#                             # board[i][j].set_number(num)
#                             tot += 1
#                     if len(board[i][j].temp_numbers) == 1:
#                         board[i][j].free = 0
#                         one_number_valid = 0
#                         if one_number_valid == 0:  ##  was = 1
#                             flag = 1  ##
#                         one_number_counter += 1
#                         board[i][j].set_number(board[i][j].temp_numbers[0])
#         kaki += 1
#     #print "The number of Free cell is ", num_of_change
#     #print "Total is ", tot
#
#
# def solution_logic2(board):
#
#     # Working func with values best
#     num_of_steps = 0
#     checking_one_number = True
#     loop = 1
#     first_time_check = 0
#     while finish_game_check(board) is not True:
#         num_of_steps += 1
#         # This loop is responsible to find all cells which have only one option valid
#         while loop == 1:
#             loop = 0
#             for i in range(9):
#                 for j in range(9):
#                     # If its empty cell we check number validity
#                     if board[i][j].free == 1:
#                         # For each number between 1-9 check if it can be valid for each cell on the board
#                         for num in range(1, 10):
#                             if check_my_row(board, num, i) is False and check_my_col(board, num, j) is False and check_num_existence_in_area_box(board, num, i, j) is False:
#                                 board[i][j].add_new_number(num)
#                         if len(board[i][j].temp_numbers) == 1:
#                             # If there is only one option which is valid for specific cell, change the number
#                             board[i][j].free = 0
#                             loop = 1
#                             board[i][j].set_number(board[i][j].temp_numbers[0])
#
#             # one_number_valid = checking_one_number(board, one_number_valid)
#             if loop == 1 and first_time_check == 0:
#                 flush_temp_number_list(board)
#
#         loop = 1
#         first_time_check = 1
#         # Running with while loop to check number validity in Box ( if there is only one option for number in box)
#         while checking_one_number:
#             checking_one_number = find_cell_place_by_number(board)
#         flush_temp_number_list(board)
#
#     print "The number of steps is {}".format(num_of_steps)
#
#
# def solution_logic3(board):
#
#     num_of_steps = 0
#     checking_one_number = True
#     checking_two_num = True
#     loop = 1
#     kaki = 0
#     one = 0
#     other = 0
#     two = 0
#     moma = 0
#     one_num_only = 1
#     two_count  = 0
#     time_print = 0
#     first_time_check = 0
#     while finish_game_check(board) is not True:
#     #while kaki < 11:
#         num_of_steps += 1
#         # This loop is responsible to find all cells which have only one option valid
#         while loop == 1 and one_num_only == 1:
#             loop = 0
#             moma = 0
#             one_num_only = 0
#             for i in range(9):
#                 for j in range(9):
#                     # If its empty cell we check number validity
#                     if board[i][j].free == 1:
#                         # For each number between 1-9 check if it can be valid for each cell on the board
#                         for num in range(1, 10):
#                             if check_my_row(board, num, i) is False and check_my_col(board, num, j) is False and check_num_existence_in_area_box(board, num, i, j) is False:
#                                 board[i][j].add_new_number(num)
#                         if len(board[i][j].temp_numbers) == 1:
#                             # If there is only one option which is valid for specific cell, change the number
#                             print i, j
#                             print board[i][j].temp_numbers
#                             board[i][j].free = 0
#                             one_num_only = 1
#                             moma = 1
#                             loop = 1
#                             one += 1
#                             board[i][j].set_number(board[i][j].temp_numbers[0])
#             # one_number_valid = checking_one_number(board, one_number_valid)
#             if one_num_only == 1:
#                 flush_temp_number_list(board)
#
#         if time_print == 0:
#             print "pass"
#         #number_option_print(board,10,10)
#             # concatenate_and_merge_temp_list(board, 3, 6, 3, 6)
#             #print_num_valid_options_per_box(board, 4, 3)
#         time_print = 1
#         loop = 1
#         one_num_only = 1
#         first_time_check = 1
#         # Running with while loop to check number validity in Box ( if there is only one option for number in box)
#         #number_option_print(board, 0,0)
#         #concatenate_and_merge_temp_list(board,0,3,0,3)
#         #checking_one_number = 1
#         #checking_one_number = 1
#         # TODO: check the function checking one number if it finds 2 one time number
#         guz = 0
#         while checking_one_number and guz == 0:
#             other += 1
#
#             checking_one_number = find_cell_place_by_number(board)
#         #checking_one_number = 1
#         # while checking_two_num and two_count < 1:
#         #      two += 1
#         #      two_count += 1
#         #      checking_two_num = find_cell_place_with_two_num(board)
#         # flush_temp_number_list(board)
#         # update_temp_option_per_cell(board)
#         # TODO: need to check if we need to refresh and refind before find 2 num func
#         guz = 1
#         checking_one_number = 1
#         if find_cell_place_with_two_num(board):
#             two += 1
#             print "good"
#         #number_option_print(board, 10, 10)
#         #print_num_valid_options_per_box(board, 0, 0)
#         # for i in range(9):
#         #  col_numbers_valid_print(board, i)
#         # for i in range(9):
#         #  col_numbers_valid_check(board, i)
#         # for i in range(9):
#         #  row_numbers_valid_check(board, i)
#         #print "kola" + str(board[0][8].temp_numbers[2])
#         #print 'xsxs',board[1][8].free
#         #concatenate_and_merge_temp_list(board, 0, 3, 0, 3)
#         #print_num_valid_options_per_box_row_col(board,0,0)
#         flush_temp_number_list(board)
#         kaki += 1
#         #if time_print == 0:
#         #print "pxx"
#         #two_numbers_in_temp_check(board, 3, 6, 3, 6)
#         time_print = 1
#         # concatenate_and_merge_temp_list(board, 6, 9, 6, 9)
#         # col_numbers_valid_print(board,7)
#
#
#        # two_numbers_in_temp_check(board, 0, 3, 3, 6)
#         #two_numbers_in_temp_check(board, 3, 6, 3, 6)
#         # if len(board[4][3].temp_numbers) == 2:
#         #         print "lola"
#         # elif len(board[4][3].temp_numbers) == 2:
#         #         print "kola"+str(board[4][3].temp_numbers[1])
#         # print board[4][7].free
#         # print board[4][7].temp_numbers[2]
#         #number_option_print(board, 10, 10)
#
#     #print board[10][10]
#     print "\n"
#     print "The number of steps is {}".format(num_of_steps)
#     print "one is ", one
#     print "Two is ", two
#     print "other is ", other


def main():

    first_board = build_sudoku_board_generator(5)
    sudko_board = init_sudoku_board(first_board)
    start_time = time.time()
    solution_logic(sudko_board)
    Total = time.time() - start_time

    print "\n"+"The solution for sudoku is :"+"\n"
    #number_matrix_print(sudko_board)
    sudo_style_print(sudko_board)
    print "run time = {}".format((Total))

main()
