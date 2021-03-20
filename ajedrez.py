"""Valor de las piezas
https://www.chess.com/terms/chess-piece-value
Rey = No tiene valor, pues no se puede capturar
Reina = 9
Alfil = 3.25 (Según Bobby Fischer y Kasparov)
Caballo = 3
Peón = 1
Torre = 5

Los valores de las piezas serán positivos para mí y negativos para mi oponente
Puedo crear una clase que sea la pieza, la cual va a contener su valor, posición, movidas posibles
Checar la notación FEN para generar las posiciones
El tablero va a ser una matriz, puedo usar modulo y división para encontrar la coordenada
Uso un diccionario para guardar la información de las piezas, tengo una clase por tipo de pieza 
(o un atributo que diga el tipo, por definir).
Un diccionario para las piezas blancas y un diccionario para las piezas negras. 
La llave es la coordenada, el valor es el objeto de la pieza

Movidas posibles:
    Mover hacia abajo le sumo 8
    Mover hacia arriba le resto 8
    Mover hacia la izquierda le resto 1
    Mover hacia la derecha le sumo 1
    Mover diagonalmente arriba a la derecha
    Mover diagonalmente arriba a la izquierda
    Mover diagonalmente abajo a la derecha
    Mover diagonalmente abajo a la izquierda
    Ver como demonios mover al caballo

"""

# Creo una clase que se llame tablero


class Tablero:
    def __init__(self, posiciones, piezas):
        self.posiciones = posiciones


class Pieza:
    def __init__(self, valor, posicion, movidasPosible):
        self.valor = valor


def imprimirMatriz(matriz):
    tabla = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            tabla += str(matriz[i][j])+" "
        tabla += "\n"
    print(tabla)


# La casilla se da por un número que va de 0 a 63
# Fila = num/8; Columna = num % 8
tablero = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0]
           ]

imprimirMatriz(tablero)
