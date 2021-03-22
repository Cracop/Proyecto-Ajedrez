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
Notación FEN para el inicio rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR

El tablero va a ser una matriz, puedo usar modulo y división para encontrar la coordenada
Uso un diccionario para guardar la información de las piezas, tengo una clase por tipo de pieza
(o un atributo que diga el tipo, por definir).
Un diccionario para las piezas blancas y un diccionario para las piezas negras.
La llave es la coordenada, el valor es el objeto de la pieza

Movidas posibles: Esto es para moverse un cuadrito en esas direcciones
Para más de un cuadrito lo multiplico por 2 y ya
    Mover hacia abajo le sumo 8
    Mover hacia arriba le resto 8
    Mover hacia la izquierda le resto 1
    Mover hacia la derecha le sumo 1
    Mover diagonalmente arriba a la derecha le resto 7
    Mover diagonalmente arriba a la izquierda le resto 9
    Mover diagonalmente abajo a la derecha le sumo 9
    Mover diagonalmente abajo a la izquierda le sumo 7
    +Ver como demonios mover al caballo
      19  21     le resto 17 o 15
    26      30   le resto 10 o 6
        36
    42      46   le sumo 6 o 10
      51  53     le sumo 15 o 17

tipos:
    P - Peon
    C - Caballo
    A - Alfil
    T - Torre
    D - Dama
    R - Rey

    XN - Pieza negra
    XB - pieza blanca

Para las heurísticas puedo utilizar la heurística material (sumo el valor de las piezas)
y hay heuristicas para cada tipo de pieza, dependiendo de donde este en el tablero se le da un valor
"""
import heuristicas as h


class Tablero:
    def __init__(self, posiciones, piezas):
        self.posiciones = posiciones


class Pieza:
    def __init__(self, posicion, nombre, tipo):
        self.posicion = posicion
        self.nombre = nombre
        self.tipo = tipo
        self.movidas = []


def imprimirMatriz(matriz):
    tabla = ""
    num = 0
    for i in range(len(matriz)):
        tabla += "|"
        for j in range(len(matriz[i])):
            if (matriz[i][j] == 0):
                #tabla += str(matriz[i][j]+num)+" "
                tabla += ".."
                tabla += "|"
            else:
                tabla += matriz[i][j].nombre
                tabla += "|"
            num += 1
        tabla += "\n"
    print(tabla)


"""Rey = No tiene valor, pues no se puede capturar, pero necesito un valor para la heuristica
Reina = 9
Alfil = 3.25 (Según Bobby Fischer y Kasparov)
Caballo = 3
Peón = 1
Torre = 5"""
# La casilla se da por un número que va de 0 a 63
# Fila = num/8; Columna = num % 8


def crearPiezas(matriz, blancas, negras, FEN):
    FEN = FEN.replace('/', '')
    # Va de abajo hacia arriba, minusculas son negras, mayusculas son blancas
    num = 0
    for i in range(len(FEN)):
        if FEN[i].isnumeric():
            num += int(FEN[i])
            num -= 1
        if FEN[i] == "r":  # Torre negra
            torre = Pieza(num, "Tn", "Torre")
            matriz[int(num/8)][num % 8] = torre
            negras[num] = torre
        elif FEN[i] == "n":  # caballo negro
            caballo = Pieza(num, "Cn", "Caballo")
            matriz[int(num/8)][num % 8] = caballo
            negras[num] = caballo
        elif FEN[i] == "b":  # alfil negro
            alfil = Pieza(num, "An", "Alfil")
            matriz[int(num/8)][num % 8] = alfil
            negras[num] = alfil
        elif FEN[i] == "q":  # dama negra
            dama = Pieza(num, "Dn", "Dama")
            matriz[int(num/8)][num % 8] = dama
            negras[num] = dama
        elif FEN[i] == "k":  # rey negro
            rey = Pieza(num, "Rn", "Rey")
            matriz[int(num/8)][num % 8] = rey
            negras[num] = rey
        elif FEN[i] == "p":  # peon negro
            peon = Pieza(num, "Pn", "Peon")
            matriz[int(num/8)][num % 8] = peon
            negras[num] = peon
        elif FEN[i] == "P":  # peon blanco
            peon = Pieza(num, "Pb", "Peon")
            matriz[int(num/8)][num % 8] = peon
            blancas[num] = peon
        if FEN[i] == "R":  # Torre negra
            torre = Pieza(num, "Tb", "Torre")
            matriz[int(num/8)][num % 8] = torre
            blancas[num] = torre
        elif FEN[i] == "N":  # caballo negro
            caballo = Pieza(num, "Cb", "Caballo")
            matriz[int(num/8)][num % 8] = caballo
            blancas[num] = caballo
        elif FEN[i] == "B":  # alfil negro
            alfil = Pieza(num, "Ab", "Alfil")
            matriz[int(num/8)][num % 8] = alfil
            blancas[num] = alfil
        elif FEN[i] == "Q":  # dama negra
            dama = Pieza(num, "Db", "Dama")
            matriz[int(num/8)][num % 8] = dama
            blancas[num] = dama
        elif FEN[i] == "K":  # rey negro
            rey = Pieza(num, "Rb", "Rey")
            matriz[int(num/8)][num % 8] = rey
            blancas[num] = rey
        num += 1


tablero = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0]
           ]

# Diccionario, sus llaves son la posiciones y el valor es el objeto de la pieza
piezasBlancas = {}
piezasNegras = {}
# Notacion FEN, con esto puedo dar un estado del tablero
FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
crearPiezas(tablero, piezasBlancas, piezasNegras, FEN)
imprimirMatriz(tablero)

print(str(h.heuristicaMaterial(piezasBlancas, piezasNegras)))
