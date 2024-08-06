import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move
from ..othello.gamestate import GameState
# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

EVAL_TEMPLATE = [
    [100, -30, 6, 2, 2, 6, -30, 100],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [100, -30, 6, 2, 2, 6, -30, 100]
]

def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada 
    # Remova-o e coloque uma chamada para o minimax_move (que vc implementara' no modulo minimax).
    # A chamada a minimax_move deve receber sua funcao evaluate como parametro.

    return minimax_move(state, 4, evaluate_custom)


def evaluate_custom(state, player:str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on your custom heuristic
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    num_pieces = state.board.num_pieces('W') + state.board.num_pieces('B')
    if (num_pieces <= 20):
        return (85*evaluate_mask(state, player) + 15*evaluate_stability(state, player))/100
        
    elif (num_pieces <= 40):
        return (50*evaluate_mask(state, player) + 30*evaluate_moves(state, player) + 20*evaluate_stability(state, player))/100

    return (30*evaluate_count(state, player) + 30*evaluate_moves(state, player) + 40*evaluate_stability(state, player))/100

def evaluate_mask(state, player:str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on the positional value of the pieces.
    You must use the EVAL_TEMPLATE above to compute the positional value of the pieces.
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    board = state.board
    countB = 0
    countW = 0
    for i in range(8):
        for j in range(8):
            piece = board.tiles[i][j]
            if piece == 'B':
                countB += EVAL_TEMPLATE[i][j]
            elif piece == 'W':
                countW += EVAL_TEMPLATE[i][j]

    if player == 'B':
        return countB - countW

    else:
        return countW - countB
    
def evaluate_count(state, player: str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on the number of pieces of each color.
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    board = state.board
    countB = board.num_pieces('B')
    countW = board.num_pieces('W')

    if player == 'B':
        return countB - countW

    else:
        return countW - countB
    
def evaluate_moves(state, player: str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on the number of legal moves.
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    board = state.board
    countB = len(board.legal_moves('B'))
    countW = len(board.legal_moves('W'))
    if player == 'B':
        return countB - countW
    else:
        return countW - countB
    #return len(state.board.legal_moves(player))

def evaluate_stability(state, player: str) -> float:
    stable_count = 0
    for x in range(8):
        for y in range(8):
            if is_stable(state, x, y, player):
                stable_count += 1
    return stable_count

def is_stable(state, x, y, player):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)] 

    if state.board.tiles[y][x] != player:
        return False

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        while is_on_board(nx, ny):
            if state.board.tiles[ny][nx] != player:
                return False
            nx += dx
            ny += dy

    return True

def is_on_board(x, y):
    return 0 <= x < 8 and 0 <= y < 8
