from algo.state import State


def alpha_beta(initial_state: State, depth):
    eval, action, total_nodes_exploration = player_max(initial_state, depth, float('-inf'), float('inf'), 0)
    print("Nombre de noeuds explorés alpha beta: ", total_nodes_exploration)
    return action


def player_max(state: State, depth, alpha, beta, total_nodes):
    if depth == 0 or state.is_terminal():
        return state.evalTotal(), None, total_nodes

    u = float('-inf')
    best_action = None

    for a in state.possible_actions():
        son = state.copy()
        total_nodes += 1
        son.make_action(a)
        son.change_player()

        v, _, total_nodes = player_min(son, depth - 1, alpha, beta, total_nodes)

        if v > u:
            u = v
            best_action = a

        alpha = max(alpha, u)
        if beta <= alpha:
            break

    return u, best_action, total_nodes


def player_min(state: State, depth, alpha, beta, total_nodes):
    if state.is_terminal() or depth == 0:
        return state.evalTotal(), None, total_nodes

    u = float('inf')
    best_action = None

    for a in state.possible_actions():
        son = state.copy()
        total_nodes += 1
        son.make_action(a)
        son.change_player()

        v, _, total_nodes = player_max(son, depth - 1, alpha, beta, total_nodes)

        if v < u:
            u = v
            best_action = a

        beta = min(beta, u)
        if beta <= alpha:
            break

    return u, best_action, total_nodes
