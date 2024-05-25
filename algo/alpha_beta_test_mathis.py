from algo.state import State


def alpha_beta(initial_state: State, depth):
    eval, action = player_max(initial_state, depth, float('-inf'), float('inf'))
    return action


def player_max(state: State, depth, alpha, beta):
    if depth == 0 or state.is_terminal():
        return state.evalTotal(), None

    u = float('-inf')
    best_action = None

    for a in state.possible_actions():
        son = state.copy()
        son.make_action(a)
        son.change_player()

        v, _ = player_min(son, depth - 1, alpha, beta)

        if v > u:
            u = v
            best_action = a

        alpha = max(alpha, u)
        if beta <= alpha:
            break

    return u, best_action


def player_min(state: State, depth, alpha, beta):
    if state.is_terminal() or depth == 0:
        return state.evalTotal(), None

    u = float('inf')
    best_action = None

    for a in state.possible_actions():
        son = state.copy()
        son.make_action(a)
        son.change_player()

        v, _ = player_max(son, depth - 1, alpha, beta)

        if v < u:
            u = v
            best_action = a

        beta = min(beta, u)
        if beta <= alpha:
            break

    return u, best_action
