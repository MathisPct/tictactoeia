from algo.alpha_beta.node_alpha_beta import NodeAlphaBeta


def alpha_beta(root_player, depth):
    max_value, action = player_max(root_player, depth, -1000000000, 1000000000)
    return action


def is_leaf(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "":
                return False
    return True


def player_max(node, depth, alpha, beta):
    if depth == 0 or is_leaf(node.Grid):
        return node.evalTotal(), None

    max_value = -1000000000
    action = None

    for row in range(len(node.Grid)):
        for col in range(len(node.Grid[row])):
            if node.Grid[row][col] == '':
                new_board = [r.copy() for r in node.Grid]
                new_board[row][col] = node.player
                evaluation, _ = player_min(
                    NodeAlphaBeta(new_board, 'O' if node.player == 'X' else 'X', node.size_of_win), depth - 1,
                    alpha, beta)
                if evaluation > max_value:
                    max_value = evaluation
                    action = new_board
                alpha = max(alpha, max_value)

                if alpha >= beta:
                    return max_value, action

    return max_value, action


def player_min(node, depth, alpha, beta):
    if depth == 0 or is_leaf(node.Grid):
        return node.evalTotal(), None

    min_value = 1000000000
    action = None

    for row in range(len(node.Grid)):
        for col in range(len(node.Grid[row])):
            if node.Grid[row][col] == '':
                new_board = [r.copy() for r in node.Grid]
                new_board[row][col] = node.player

                evaluation, _ = player_max(
                    NodeAlphaBeta(new_board, 'O' if node.player == 'X' else 'X', node.size_of_win),
                    depth - 1, alpha, beta)
                if evaluation < min_value:
                    min_value = evaluation
                    action = new_board
                beta = min(beta, min_value)

                if alpha >= beta:
                    return min_value, action

    return min_value, action
