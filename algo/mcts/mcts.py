import math
import random

from algo.mcts.node_mcts import NodeMcts


def uct_search(root, current_turn, size_of_win):
    """Monte Carlo Tree Search"""
    root = NodeMcts(root.Grid, current_turn, size_of_win)
    for _ in range(1000):
        node = TreePolicy(root)
        reward = estimate_victory(node)
        backup(node, reward)
    return best_child(root, 0)


def TreePolicy(node):
    while node.is_non_terminal():
        if not node.is_fully_expanded():
            return expand(node)
        else:
            node = best_child(node, math.sqrt(2))
    return node


def expand(node):
    for i in range(len(node.Grid)):
        for j in range(len(node.Grid)):
            if node.Grid[i][j] == '':
                new_board = [row[:] for row in node.Grid]
                next_turn = '0' if node.player == 'X' else 'X'
                new_board[i][j] = next_turn
                unvisited_node = NodeMcts(new_board, next_turn, node.size_of_win, node)
                node.children.append(unvisited_node)
                return unvisited_node


def best_child(node, constante_divergence):
    max = 0
    max_child = None

    for child in node.children:
        if node.score==0 or child.score==0:
            score=math.inf
        else:
            if child.nb_passage==0:
                print("nb_passage: ", child.nb_passage)
            if child.score == 0:
                print("child.score: ", child.score())
            if node.score== 0:
                print("node.score: ", node.score)

            try:
                score = child.score / child.nb_passage + constante_divergence * (math.sqrt((2 * math.log(node.score)) / child.score))
            except ValueError:
                print("child nb passage", child.nb_passage)
                print("child score: ", child.score)
                print("parent score: ", node.score)

        if score > max:
            max = score
            max_child = child

    return max_child


def backup(v, reward):
    current_node = v
    while current_node is not None:
        current_node.nb_passage += 1
        current_node.score += reward
        reward = -reward
        current_node = current_node.parent


def estimate_victory(node):
    list_action = []
    board = [row[:] for row in node.Grid]
    estimated_node = NodeMcts(board, 'O' if node.player == 'X' else 'X', node.size_of_win)

    for i in range(len(estimated_node.board)):
        for j in range(len(estimated_node.board)):
            if estimated_node.board[i][j] == '':
                list_action.append((i, j))

    while len(list_action) > 0:
        position = random.choice(list_action)
        estimated_node.board[position[0]][position[1]] = estimated_node.current_turn
        list_action.remove(position)

        is_winning = estimated_node.is_winning(position[0], position[1])

        if is_winning and estimated_node.current_turn == node.player:
            return 1

        elif is_winning and estimated_node.current_turn != node.player:
            return -1

        estimated_node.current_turn = 'O' if estimated_node.current_turn == 'X' else 'X'

    return 0
