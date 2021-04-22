from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import render

from IA.ajedrez import Juego as Game
import chess


game = Game()


def index(request):
    return render(request, "build/index.html")


@api_view(['GET', 'POST'])
def comenzarJuego(request):
    #game = Game()
    if request.method == 'GET':
        game = Game()
        game.imprimetablero()
        return Response({
            'status': 'game start',
        })


@api_view(['GET'])
def movimiento(request, move, mode):
    if request.method == 'GET':
        objectMove = game.darJugadaParam(move)
        if objectMove == "Jugada inválida":
            return Response({
                'status': 'game continue',
                'isValid': False,
            })
        else:
            print(objectMove)
            game.tablero.push(objectMove)
            objectPCMove = game.seleccionaMovimiento(game, mode)
            pcMove = str(objectPCMove["move"])
            game.tablero.push(objectPCMove["move"])
            game.imprimetablero()
            return Response({
                'status': objectPCMove["GameOver"],
                'isValid': True,
                'move': pcMove,
            })


@api_view(['GET'])
def automatic_move(request, level):
    if request.method == 'GET':
        move = game.seleccionaMovimiento(game, level)
        print(move)
        if move["GameOver"]:
            return Response({
                'status': 'gameOver',
            })
        else:
            game.tablero.push(move["move"])
            game.imprimetablero()
            return Response({
                'status': 'game continue',
                'move': str(move["move"]),
            })
