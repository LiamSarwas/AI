import GameTree


class AlphaBeta:
    def __init__(self):
        pass

    @staticmethod
    def alpha_beta_search(game_tree):
        infinity = float('inf')
        best_val = -infinity
        beta = infinity

        successors = AlphaBeta.get_successors(game_tree)
        best_state = None
        for state in successors:
            value = AlphaBeta.min_value(state, best_val, beta)
            if value > best_val:
                best_val = value
                best_state = state

        return best_state

    @staticmethod
    def max_value(node, alpha, beta):

        if AlphaBeta.is_terminal(node):
            return AlphaBeta.get_utility(node)

        infinity = float('inf')
        value = -infinity

        successors = AlphaBeta.get_successors(node)
        for state in successors:
            value = max(value, AlphaBeta.min_value(state, alpha, beta))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value

    @staticmethod
    def min_value(node, alpha, beta):

        if AlphaBeta.is_terminal(node):
            return AlphaBeta.get_utility(node)
        infinity = float('inf')
        value = infinity

        successors = AlphaBeta.get_successors(node)
        for state in successors:
            value = min(value, AlphaBeta.max_value(state, alpha, beta))
            if value <= alpha:
                return value
            beta = min(beta, value)

        return value

    @staticmethod
    def get_successors(node):
        assert node is not None
        return node.children

    @staticmethod
    def is_terminal(node):
        assert node is not None
        return len(node.children) == 0

    @staticmethod
    def get_utility(node):
        assert node is not None
        return AlphaBeta.evaluate(node.value)

    @staticmethod
    def evaluate(game):
        # I use an advanced heuristic based on weightings from the work
        # Design of Artificial Intelligence for Mancala Games by Gabriele Rovaris

        if game is None:
            return 0

        # weights
        w1 = 0.2
        w2 = 0.2
        w3 = 0.4
        w4 = 1
        w5 = 0.55

        # heuristics
        h1 = game.board[0]

        h2 = 0
        for i in range(0, 6):
            h2 += game.board[i]

        h3 = 0
        for i in range(0, 6):
            if game.board != 0:
                h3 += 1

        h4 = game.board[6]

        h5 = game.board[13]

        return h1*w1 + h2*w2 + h3*w3 + h4*w4 - h5*w5
