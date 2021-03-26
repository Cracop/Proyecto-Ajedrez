#Importo la librería
import chess 
import random
#Esto me genera el tablero, si no le paso parametros me lo crea en la posición inicial.
#Como parametro le tengo que pasar un estado en notacion FEN
tablero = chess.Board()
#print(tablero)
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

     0  1  2  3  4  5  6  7
     8  9 10 11 12 13 14 15
    16 17 18 19 20 21 22 23
    24 25 26 27 28 29 30 31
    32 33 34 35 36 37 38 39
    40 41 42 43 44 45 46 47
    48 49 50 51 52 53 54 55
    56 57 58 59 60 61 62 63 

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
#   chess.square_name(0) me regresa sus coordenadas tipo a1
#   chess.parse_square("a1") me regresa su número tipo 0

#De igual manera puedo saber que pieza hay utilizando el número de 0 a 63,
#me regresa una letra (en realidad todo el objeto) si hay pieza, y None si no hay nada
#   tablero.piece_at(0)

for i in chess.SQUARES:
    #print(chess.SQUARES[i])
    #print(tablero.piece_at(i).color)
    pass

#Para generar la lista de movimientos posibles, me regresa algo parecido a una lista
#  tablero.legal_moves 
#   una movida esta dada posInicialPosFinal i.e. a2a3 un peon blanco avanza un cuadrado
#   Una movida pertenece a una clase específica

#Para hacer que se haga una movida
#   tablero.push(movida)
#   hasta ahorita solo he logrado que lo haga iterando sobre la lista, no al darsela yo

#Para regresar la ultima movida hecha
#   tablero.pop()
#   como una lista

#El turno del que tiene que jugar esta dado por
#   tablero.turn = Boolan
#Donde 
#   False = negras
#   True = blancas
#Si quiero elegir una movida de forma aleatoria
#   movida = random.choice([movida for movida in tablero.legal_moves])

#El siguiente codigo hace una partida con ambos lados haciendo movidas aleatorias
#print(tablero)
"""
for i in range(500):
    #print("Turno de", tablero.turn)
    if tablero.is_game_over():
        print("Se acabo el juego", i)
        break
    movida = random.choice([movida for movida in tablero.legal_moves])
    tablero.push(movida)
    print(tablero)
    print("")
print(tablero)

#   Al momento de hacer el push y pop me cambia el turno

#Para hacer una movida dada de manera especifica
#   Al parecer se por medio de numeros del 0 al 63
#   movida = chess.Move(fromSquare, toSqcuare)

print(tablero)
movida = chess.Move(1,25)
tablero.push(movida)
print(movida)
print(tablero)
"""
#Falta enteder bien como esta dado el tablero, así que primero haré una funcion para 
#   imprimir esto
def imprimeTablero(tablero):
    texto=""
    texto += "8 "
    texto+=obtenFila(56,64, tablero)
    texto += "7 "
    texto+=obtenFila(48,56, tablero)
    texto += "6 "
    texto+=obtenFila(40,48, tablero)
    texto += "5 "
    texto+=obtenFila(32,40, tablero)
    texto += "4 "
    texto+=obtenFila(24,32, tablero)
    texto += "3 "
    texto+=obtenFila(16,24, tablero)
    texto += "2 "
    texto+=obtenFila(8,16, tablero)
    texto += "1 "
    texto+=obtenFila(0,8, tablero) 
    texto += "  a b c d e f g h"
    print(texto)
    #print(tablero)

def obtenFila(comienzo, final, tablero):
    fila = ""
    for i in range(comienzo, final):
        if tablero.piece_at(i) == None:
            fila+=". "
        else:
            fila+=str(tablero.piece_at(i))+" "
    fila+="\n"
    return fila


"""
print("Turno de", tablero.turn, "\n")
print(tablero, "\n")
movida = chess.Move(1,16)
tablero.push(movida)
print("Turno de", tablero.turn , "\n")
print(tablero, "\n")
print("Ultima movida",tablero.peek())
print("Turno de", tablero.turn , "\n")
print(tablero)
"""
"""
print(tablero)
for i in range(5):
    movida = random.choice([movida for movida in tablero.legal_moves])
    tablero.push(movida)
    print("")
    print(tablero)
"""
#print(tablero)
#print(tablero.legal_moves)

imprimeTablero(tablero)
ino=input("Coloca la movida que quieras ")
#ino="a2a3"
try:
    movida = chess.Move(chess.parse_square(ino[0:2]),chess.parse_square(ino[2:4]))
    if movida in tablero.legal_moves:
        tablero.push(movida)
    else: 
        print("Movida ilegal")
except:
    print("Coordenada inválida")
imprimeTablero(tablero)
print(tablero.is_checkmate())
print(tablero.result())