import random


class Owari():
    NORTH = True
    SOUTH = False

    def __init__(self):
        self.board = [3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 0]
        self.player = self.get_first_player()
        # self.player = self.NORTH

    def get_board(self):
        return self.board

    def get_score(self):
        return self.board[6], self.board[13]

    def is_game_over(self):
        is_over = True

        # check if SOUTH is empty
        for i in range(0, 6):
            if self.board[i] != 0:
                is_over = False

        if is_over:
            # empty NORTH side
            for i in range(7, 13):
                self.board[13] += self.board[i]
                self.board[i] = 0
            return True

        is_over = True

        # check if NORTH is empty
        for i in range(7, 13):
            if self.board[i] != 0:
                is_over = False

        if is_over:
            # empty SOUTH side
            for i in range(0, 6):
                self.board[6] += self.board[i]
                self.board[i] = 0

        return is_over

    def move(self, n):
        old_board = list(self.board)

        # protection from invalid moves comes from GUI?
        stones = self.board[n]
        self.board[n] = 0

        i = 0
        while stones:
            i += 1
            self.board[(n+i) % 14] += 1
            stones -= 1

        # does the last stone end in an empty pocket on the movers side
        last_pocket = (n+i) % 14
        if old_board[last_pocket] == 0:
            if self.player == self.NORTH and last_pocket in range(0, 6):
                self.board[6] += self.board[12-last_pocket]
                self.board[12-last_pocket] = 0
            if self.player == self.SOUTH and last_pocket in range(7, 13):
                self.board[13] += self.board[12 - last_pocket]
                self.board[12 - last_pocket] = 0

        return self.board

    def get_first_player(self):
        print('Would you rather go first or second?')
        while True:
            player = input('Enter 1 or 2. ')
            if player == '1':
                return self.SOUTH
            if player == '2':
                return self.NORTH
            else:
                print('Invalid selection. Please try again.')

    def set_next_player(self):
        if self.player == self.SOUTH:
            self.player = self.NORTH
        elif self.player == self.NORTH:
            self.player = self.SOUTH

    def get_valid_moves(self):
        move_list = []
        if self.player == self.SOUTH:
            for i in range(0, 6):
                if self.board[i] != 0:
                    move_list.append(i)
        else:
            for i in range(7, 13):
                if self.board[i] != 0:
                    move_list.append(i)

        self.set_next_player()
        return move_list

    def print_board(self):
        print('   ' + str(self.board[12]) + ' ' + str(self.board[11]) + ' ' + str(self.board[10]) + ' '
              + str(self.board[9]) + ' ' + str(self.board[8]) + ' ' + str(self.board[7]) + '   ')
        print(str(self.board[13]) + '              ' + str(self.board[6]))
        print('   ' + str(self.board[0]) + ' ' + str(self.board[1]) + ' ' + str(self.board[2]) + ' ' +
              str(self.board[3]) + ' ' + str(self.board[4]) + ' ' + str(self.board[5]) + '   ')
        print('\n')


def main():
    o = Owari()
    o.print_board()

    while not o.is_game_over():
        move_list = o.get_valid_moves()
        if o.player:
            print('Valid moves are: ', move_list)
            while True:
                move = input('Select a move: ')
                if int(move) in range(0, 6) and o.board[int(move)] != 0:
                    o.move(int(move))
                    break
                else:
                    print('Invalid move choice. Please try again.')

        else:
            o.move(move_list[random.randint(0, len(move_list)-1)])
        o.print_board()

    o.print_board()
    print(o.get_score())


main()
