import random


class Player():
    def __init__(self):
        self.board = []

    def get_next_move(self, board, move_list):
        return move_list[random.randint(0, len(move_list))]

    def evaluate(self, board, move_list):
