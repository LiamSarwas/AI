import Owari
import Player


def main():
    while True:
        depth_limit = input('How deep do you want to search: ')
        try:
            x = int(depth_limit)
            if x > 0:
                depth_limit = int(depth_limit)
                break
            else:
                print('Invalid search depth choice.')
        except ValueError:
            print('Invalid search depth choice.')

    o = Owari.Board()
    p = Player.Player()
    o.print_board()

    while not o.is_game_over():
        move_list = o.get_valid_moves()
        if not o.player:
            print('Valid moves are: ', move_list)
            while True:
                move = input('Select a move: ')
                try:
                    x = int(move)
                    if x > 0:
                        move = int(move)
                        if move in range(7, 13) and o.board[move] != 0:
                            o.move(move)
                            break
                        else:
                            print('Invalid move choice. Please try again.')
                    else:
                        print('Invalid move choice. Please try again.')
                except ValueError:
                    print('Invalid move choice. Please try again.')

        else:
            computer_move = p.get_next_move(o, depth_limit, 5)
            print('Computer Move: ', computer_move)
            print()
            o.move(computer_move)
        o.print_board()

    o.print_board()
    print(o.get_score())


main()
