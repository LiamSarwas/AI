import copy
import heapq
from AB_search import AlphaBeta


class GameNode:
    def __init__(self, value, move):
        self.value = value
        self.move = move
        self.children = []    # a list of nodes

    def __lt__(self, other):
        return AlphaBeta.evaluate(self.value) < AlphaBeta.evaluate(other.value)

    def add_child(self, child_node):
        self.children.append(child_node)


class GameTree:
    def __init__(self, q_depth):
        self.best_node = GameNode(None, None)
        self.quiescent_depth = q_depth

    def build_tree(self, game, depth, move=None, is_quiescent=False):
        node = GameNode(game, move)
        if depth == 0:
            if node > self.best_node and not is_quiescent:
                self.best_node = node
                moves = game.get_valid_moves()
                if len(moves) == 0:
                    return node

                for move in moves:
                    new_game = copy.deepcopy(game)
                    new_game.move(move)
                    node.add_child(self.build_tree(new_game, self.quiescent_depth, move, True))

            return node

        moves = game.get_valid_moves()
        if len(moves) == 0:
            return node

        for move in moves:
            new_game = copy.deepcopy(game)
            new_game.move(move)
            node.add_child(self.build_tree(new_game, depth-1, move))

        return node
