import random
from typing import Tuple
from ..tttm.gamestate import GameState
from ..tttm.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Retorna uma jogada calculada pelo algoritmo minimax para o estado de jogo fornecido.
    :param state: estado para fazer a jogada
    :return: tupla (int, int) com as coordenadas x, y da jogada (lembre-se: 0 é a primeira linha/coluna)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada do Jogo da Tic-Tac-Toe Misere
    # Remova-o e coloque uma chamada para o minimax_move com 
    # a sua implementacao da poda alpha-beta. Use profundidade ilimitada na sua entrega,
    # uma vez que o jogo tem profundidade maxima 9. 
    # Preencha a funcao utility com o valor de um estado terminal e passe-a como funcao de avaliação para seu minimax_move

    return minimax_move(state, -1, utility)

def utility(state:GameState, player:str) -> float:
    """
    Retorna a utilidade de um estado (terminal) 
    """
    winner = state.winner()
    if winner == player:
        return 1
    elif winner is not None:
        return -1
    else:
        return 0

    '''for i in range(3):
        if (state.board.board[i][0] == player):
            if (state.board.board[i][0] == state.board.board[i][1] or state.board.board[i][1] == state.board.board[i][2]):
                utility -= 1
                if (state.board.board[i][0] == state.board.board[i][1] and state.board.board[i][1] == state.board.board[i][2]):
                    utility -= 1

        elif (state.board.board[i][0] == oponent):
            if (state.board.board[i][0] == state.board.board[i][1] or state.board.board[i][1] == state.board.board[i][2]):
                utility += 1
                if (state.board.board[i][0] == state.board.board[i][1] and state.board.board[i][1] == state.board.board[i][2]):
                    utility += 1

        if (state.board.board[0][i] == player):
            if (state.board.board[0][i] == state.board.board[1][i] or state.board.board[1][i] == state.board.board[2][i]):
                utility -= 1
                if (state.board.board[0][i] == state.board.board[1][i] and state.board.board[1][i] == state.board.board[2][i]):
                    utility -= 1
                    
        elif(state.board.board[0][i] == oponent):
            if (state.board.board[0][i] == state.board.board[1][i] or state.board.board[1][i] == state.board.board[2][i]):
                utility += 1
                if (state.board.board[0][i] == state.board.board[1][i] and state.board.board[1][i] == state.board.board[2][i]):
                    utility += 1'''

    return utility
