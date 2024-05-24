from algo.state import State


def alpha_beta(initial_state: State, depth):
    eval, action = player_max(initial_state, depth, float('-inf'), float('inf'))
    return action


def player_max(state: State, depth, alpha, beta):
    if depth == 0 or state.is_terminal():
        return state.evalTotal(), None
    u = float('-inf')
    action = None
    for a in state.possible_actions():
        new_state = state.copy()
        new_state.make_action(a)

        new_state_other_player = new_state.copy()
        new_state_other_player.change_player()
        v, _ = player_min(new_state_other_player, depth - 1, alpha, beta)

        if v > u:
            u = v
            action = a
        if u >= beta:
            return u, action
        alpha = max(alpha, u)
        if beta <= alpha:
            return u, action
    return u, action


def player_min(state: State, depth, alpha, beta):
    if state.is_terminal() or depth == 0:
        return state.evalTotal(), None
    u = float('inf')
    action = None
    for a in state.possible_actions():
        new_state = state.copy()
        new_state.make_action(a)

        new_state_other_player = new_state.copy()
        new_state_other_player.change_player()
        v, _ = player_max(new_state, depth - 1, alpha, beta)

        if v < u:
            u = v
            action = a
        if u <= alpha:
            return u, action
        beta = min(beta, u)
        if beta <= alpha:
            return u, action
    return u, action
