import random
import math

from algo.mcts.node_mcts import NodeMcts


def uct_search(root_board, current_turn, size_of_win):
    root = NodeMcts(root_board, current_turn, size_of_win)
    for i in range(1000):
        node = tree_policy(root)
        reward = estimate_victory(node)
        backup(node, reward)
    return best_child(root, 0)


def tree_policy(node):
    while node.is_non_terminal():
        if not node.is_fully_expanded():
            return expand(node)
        else:
            node = best_child(node, math.sqrt(2))
    return node


def expand(node):
    if node.untried_moves:
        move = random.choice(node.untried_moves)
        node.untried_moves.remove(move)
        i, j = move
        next_turn = 'O' if node.current_turn == 'X' else 'X'
        new_board = [row[:] for row in node.board]
        new_board[i][j] = node.current_turn
        child_node = NodeMcts(new_board, next_turn, node.size_of_win, node)
        node.children.append(child_node)
        print(f"Expanding: Placing {node.current_turn} at ({i}, {j})")
        return child_node
    else:
        raise Exception("Should not call expand on a fully expanded node")


def best_child(node, constante_divergence):
    best_value = -float('inf')
    best_node = None

    for child in node.children:
        if child.nb_passage == 0:
            uct_value = float('inf')
        else:
            uct_value = (child.score / child.nb_passage) + constante_divergence * math.sqrt(
                math.log(node.nb_passage) / child.nb_passage)

        print(f"Child with score {child.score} and visits {child.nb_passage} has UCT value {uct_value}")

        if uct_value > best_value:
            best_value = uct_value
            best_node = child

    return best_node


def backup(node, reward):
    while node is not None:
        node.nb_passage += 1
        node.score += reward
        reward = -reward
        node = node.parent


def estimate_victory(node):
    simulated_node = NodeMcts([row[:] for row in node.board], node.current_turn, node.size_of_win)
    available_moves = [(i, j) for i in range(len(node.board)) for j in range(len(node.board[i])) if node.board[i][j] == '']
    current_turn = node.current_turn

    while available_moves:
        x, y = random.choice(available_moves)
        available_moves.remove((x, y))
        simulated_node.board[x][y] = current_turn
        if simulated_node.is_winning(x, y):
            return 1 if current_turn == node.current_turn else -1
        current_turn = 'O' if current_turn == 'X' else 'X'

    return 0


