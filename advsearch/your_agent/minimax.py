import random
from typing import Tuple, Callable
from ..tttm.gamestate import GameState



def minimax_move(state:GameState, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    v, a = MAX(state, float('-inf'), float('inf'), eval_func)
    return a

def MAX(state:GameState, alpha, beta, eval_func:Callable):
    if state.is_terminal():
        return eval_func(state, state.player), None
    
    v = float('-inf')
    a = None
    
    moves = state.legal_moves()
    for move in moves:
        next_state = state.next_state(move)
        v_min,_ = MIN(next_state, alpha, beta, eval_func)
        if (v_min > v):
            v = v_min
            a = move
        alpha = max(alpha, v)
        if (alpha >= beta):
            break
    return v, a

def MIN(state:GameState, alpha, beta, eval_func:Callable):
    if state.is_terminal():
        return eval_func(state, state.player), None
    
    v = float('inf')
    a = None
    
    moves = state.legal_moves()
    for move in moves:
        next_state = state.next_state(move)
        v_max, _ = MAX(next_state, alpha, beta, eval_func)
        if (v_max < v):
            v = v_max
            a = move
        beta = min(beta, v)
        if (beta <= alpha):
            break
    return v, a


