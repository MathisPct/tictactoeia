def min_max(root_player, depth):
    max_value, action = player_max(root_player, depth)
    return action

def player_max(node, depth):
    if len(node.children_node) == 0:
        node.generate_children()

    if depth == 0 or node.is_leaf():
        return node.evalTotal(), node.board

    max_value = -1000000000
    action = None

    for child_node in node.children_node:
        evaluation, _ = player_min(child_node, depth - 1)
        if evaluation > max_value:
            max_value = evaluation
            action = child_node.board

    return max_value, action


def player_min(node, depth):
    if len(node.children_node) == 0:
        node.generate_children()

    if depth == 0 or node.is_leaf():
        return node.evalTotal(), node.board

    min_value = 1000000000
    action = None

    for child_node in node.children_node:
        evaluation, _ = player_max(child_node, depth - 1)
        #print(str(evaluation), " :")
        #print(str(child_node.board[0]))
        #print(str(child_node.board[1]))
        #print(str(child_node.board[2]))
        if evaluation < min_value:
            min_value = evaluation
            action = child_node.board

    return min_value, action
