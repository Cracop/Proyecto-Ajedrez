#Importo la librería
import chess 
import random

def imprimeTablero(tablero):
    texto=""
    texto += "8|"
    texto+=obtenFila(56,64, tablero)
    texto += "7|"
    texto+=obtenFila(48,56, tablero)
    texto += "6|"
    texto+=obtenFila(40,48, tablero)
    texto += "5|"
    texto+=obtenFila(32,40, tablero)
    texto += "4|"
    texto+=obtenFila(24,32, tablero)
    texto += "3|"
    texto+=obtenFila(16,24, tablero)
    texto += "2|"
    texto+=obtenFila(8,16, tablero)
    texto += "1|"
    texto+=obtenFila(0,8, tablero) 
    texto += "  - - - - - - - -\n"
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

def main():
    tablero = chess.Board()
    while not tablero.is_game_over():
        imprimeTablero(tablero)
        #print(tablero.turn)
        if tablero.turn:
            """
            ins = input("Da la movida que quieras hacer con el formato a1a2\n")
            try:
                movida = chess.Move(chess.parse_square(ins[0:2]),chess.parse_square(ins[2:4]))
                if movida in tablero.legal_moves:
                    tablero.push(movida)
                    print("las blancas movieron", movida)
                else: 
                    print("Movida ilegal")
            except:
                print("Coordenada inválida")
            """
            movida = random.choice([movida for movida in tablero.legal_moves])
            tablero.push(movida)
            print("las blancas movieron", movida)
        else:
            movida = random.choice([movida for movida in tablero.legal_moves])
            tablero.push(movida)
            print("las negras movieron", movida)
    imprimeTablero(tablero)
    print(tablero.result())


if __name__ == "__main__":
    main()