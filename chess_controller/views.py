from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from IA.ajedrez import Juego as Game
import chess

game = Game()


@api_view(['GET', 'POST'])
def comenzarJuego(request):
    #game = Game()
    if request.method == 'GET':
        game.imprimetablero()
        return Response({
            'status': 'game start',
        })


@api_view(['GET'])
def movimiento(request, move):
    if request.method == 'GET':
        # inicio = chess.parse_square(move[0:2])
        # fin = chess.parse_square(move[2:4])
        # move = chess.Move(inicio, fin)
        # if chess.Move(inicio, fin) in game.tablero.legal_moves:
        #     return Response({
        #         'status': 'prueba',
        #         'is valid': True,
        #     })

        objectMove = game.darJugadaParam(move)
        if objectMove == "Jugada inválida":
            return Response({
                'status': 'game continue',
                'isValid': False,
            })
        else:
            print(objectMove)
            game.tablero.push(objectMove)
            objectPCMove = game.seleccionaMovimiento(0)
            pcMove = str(objectPCMove)
            game.tablero.push(objectPCMove)
            game.imprimetablero()
            return Response({
                'status': 'game continue',
                'isValid': True,
                'move': pcMove,
            })
