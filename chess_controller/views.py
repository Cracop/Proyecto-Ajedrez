from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from IA.ajedrez import Juego as Game

game = Game()


@api_view(['GET', 'POST'])
def comenzarJuego(request):

    if request.method == 'GET':
        game.imprimetablero()
        return Response({
            'status': 'game start',
        })


@api_view(['GET'])
def movimiento(request, move):
    if request.method == 'GET':
        nextMove = game.darJugada(move)
        game.imprimetablero()
        return Response({
            'status': 'game continue',
            'isValid': True,
            'nextMove': nextMove,
        })
