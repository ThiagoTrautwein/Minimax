import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from ..your_agent.othello_minimax_custom import evaluate_custom
from ..your_agent.minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state. 
    Consider that this will be called in the Othello tournament situation,
    so you should call the best implementation you got.

    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada 
    # Remova-o e coloque a sua implementacao da poda alpha-beta

    return minimax_move(state, 4, evaluate_custom)


