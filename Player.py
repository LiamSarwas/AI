from GameTree import GameTree
from AB_search import AlphaBeta


class Player:
    def __init__(self):
        pass

    @staticmethod
    def get_next_move(game, depth, quiescent_depth):
        gt = GameTree(quiescent_depth)
        game_tree = gt.build_tree(game, depth)
        best_node = AlphaBeta.alpha_beta_search(game_tree)

        return best_node.move
