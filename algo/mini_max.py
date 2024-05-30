from algo.state import State


def min_max(root: State, depth):
    eval_solution, action, total_nodes_exploration = player_max(root, depth, 0)
    print("Nombre de noeuds explorés minimax: ", total_nodes_exploration)
    return action


def player_max(state: State, depth, total_nodes):
    if depth == 0 or state.is_terminal():
        return state.evalTotal(), None, total_nodes

    u = float('-inf')
    best_action = None

    for a in state.possible_actions():
        son = state.copy()
        total_nodes += 1
        son.make_action(a)
        son.change_player()

        v, _, total_nodes = player_min(son, depth - 1, total_nodes)

        if v > u:
            u = v
            best_action = a

    return u, best_action, total_nodes


def player_min(state: State, depth, total_nodes):
    if state.is_terminal() or depth == 0:
        return state.evalTotal(), None, total_nodes

    u = float('inf')
    best_action = None

    for a in state.possible_actions():
        son = state.copy()
        total_nodes += 1
        son.make_action(a)
        son.change_player()

        v, _, total_nodes = player_max(son, depth - 1, total_nodes)

        if v < u:
            u = v
            best_action = a

    return u, best_action, total_nodes
