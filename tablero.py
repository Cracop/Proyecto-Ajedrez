#Importo la librería
import chess 

#Esto me genera el tablero, si no le paso parametros me lo crea en la posición inicial.
#Como parametro le tengo que pasar un estado en notacion FEN
tablero = chess.Board()
print(tablero)
#Chess-SQUARES en un rango que va de 0 a 63
"""
SQUARES = [
    A1, B1, C1, D1, E1, F1, G1, H1,
    A2, B2, C2, D2, E2, F2, G2, H2,
    A3, B3, C3, D3, E3, F3, G3, H3,
    A4, B4, C4, D4, E4, F4, G4, H4,
    A5, B5, C5, D5, E5, F5, G5, H5,
    A6, B6, C6, D6, E6, F6, G6, H6,
    A7, B7, C7, D7, E7, F7, G7, H7,
    A8, B8, C8, D8, E8, F8, G8, H8,
] = range(64)
a1 = 0 y así sucesivamente
a1 se encuentra en la esquina inferior izquierda
a2 se encuentra a la derecha de a1
Basicamente tengo que reflejar SQUARES verticalmente
"""
#Las el color de las piezas está dado por un booleano
#   True si es blanco
#   False si es negro
#   Impriendo el teclado, las letras mayusculas son las blancas

#Piezas
#   P/p - peon
#   N/n - caballo
#   B/b - alfil
#   Q/q - Dama
#   K/k - Rey
#   R/r - Torre

#Para saber las coordenadas de la casilla dado su número de 0 a 63
#   chess.square_name(0)

#De igual manera puedo saber que pieza hay utilizando el número de 0 a 63,
#me regresa una letra (en realidad todo el objeto) si hay pieza, y None si no hay nada
#   tablero.piece_at(0)

for i in chess.SQUARES:
    #print(chess.SQUARES[i])
    #print(tablero.piece_at(i).color)
    pass

