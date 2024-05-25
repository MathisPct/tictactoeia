import math


def min_max(root_player, depth):
    max_value, action = player_max(root_player, depth,"X" if root_player.current_turn == "O" else "O")
    return action

def player_max(node, depth, root_player_sign):
    if len(node.children_node)==0:
        node.generate_children()

    if depth == 0 or node.is_leaf():
        return node.evalTotal(root_player_sign), node.board

    max_value = -math.inf
    action = None

    for child_node in node.children_node:
        evaluation, _ = player_min(child_node, depth - 1, root_player_sign)
        #print("max = ",evaluation)
        #print("\n")
        if evaluation > max_value:
            max_value = evaluation
            action = child_node.board


    #print("JE PREND LE MAX: ")
    #for i in range(len(action)):
        #print(action[i])
    #print("MAX = ",max_value)
    return max_value, action


def player_min(node, depth, root_player_sign):
    if len(node.children_node) == 0:
        node.generate_children()

    if depth == 0 or node.is_leaf():
        return node.evalTotal(root_player_sign), node.board

    min_value = math.inf
    action = None

    for child_node in node.children_node:
        evaluation, _ = player_max(child_node, depth - 1, root_player_sign)
        #print("min = ",evaluation)
        if evaluation < min_value:
            min_value = evaluation
            action = child_node.board
    #print("JE PREND LE MIN: ")
    #for i in range(len(action)):
        #print(action[i])
    #print("MIN = ", min_value)
    #print("\n")
    return min_value, action
