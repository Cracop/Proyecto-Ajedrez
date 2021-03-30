#Importo la librería
import chess 
import random

pawntable = [
 0,  0,  0,  0,  0,  0,  0,  0,
 5, 10, 10,-20,-20, 10, 10,  5,
 5, -5,-10,  0,  0,-10, -5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5,  5, 10, 25, 25, 10,  5,  5,
10, 10, 20, 30, 30, 20, 10, 10,
50, 50, 50, 50, 50, 50, 50, 50,
 0,  0,  0,  0,  0,  0,  0,  0]

knightstable = [
-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  5,  5,  0,-20,-40,
-30,  5, 10, 15, 15, 10,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 10, 15, 15, 10,  0,-30,
-40,-20,  0,  0,  0,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50]

bishopstable = [
-20,-10,-10,-10,-10,-10,-10,-20,
-10,  5,  0,  0,  0,  0,  5,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10,-10,-10,-10,-10,-20]

rookstable = [
  0,  0,  0,  5,  5,  0,  0,  0,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
  5, 10, 10, 10, 10, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0]

queenstable = [
-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  5,  5,  5,  5,  5,  0,-10,
  0,  0,  5,  5,  5,  5,  0, -5,
 -5,  0,  5,  5,  5,  5,  0, -5,
-10,  0,  5,  5,  5,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20]

kingstable = [
 20, 30, 10,  0,  0, 10, 30, 20,
 20, 20,  0,  0,  0,  0, 20, 20,
-10,-20,-20,-20,-20,-20,-20,-10,
-20,-30,-30,-40,-40,-30,-30,-20,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30]



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

def obtenFila(comienzo, final, tablero):
    fila = ""
    for i in range(comienzo, final):
        if tablero.piece_at(i) == None:
            fila+=". "
        else:
            fila+=str(tablero.piece_at(i))+" "
    fila+="\n"
    return fila

def evaluar(tablero):
    
    if tablero.is_checkmate():
        if tablero.turn:
            return -9999
        else:
            return 9999
    elif tablero.is_stalemate():
        return 0
    elif tablero.is_insufficient_material():
        return 0
    else:
        peonB = len(tablero.pieces(chess.PAWN, chess.WHITE))
        peonN = len(tablero.pieces(chess.PAWN, chess.BLACK))
        caballoB = len(tablero.pieces(chess.KNIGHT, chess.WHITE))
        caballoN = len(tablero.pieces(chess.KNIGHT, chess.BLACK))
        alfilB = len(tablero.pieces(chess.BISHOP, chess.WHITE))
        alfilN = len(tablero.pieces(chess.BISHOP, chess.BLACK))
        torreB = len(tablero.pieces(chess.ROOK, chess.WHITE))
        torreN = len(tablero.pieces(chess.ROOK, chess.BLACK))
        reinaB = len(tablero.pieces(chess.QUEEN, chess.WHITE))
        reinaN = len(tablero.pieces(chess.QUEEN, chess.BLACK))
    
        valorMaterial = 100 * (peonB - peonN) + 320 * (caballoB - caballoN) + 330 * (alfilB - alfilN) + 500 * (torreB - torreN) + 900 * (reinaB - reinaN)
        
        peonPos = sum([pawntable[i] for i in tablero.pieces(chess.PAWN, chess.WHITE)]) + sum([-pawntable[chess.square_mirror(i)] for i in tablero.pieces(chess.PAWN, chess.BLACK)])
        caballoPos = sum([knightstable[i] for i in tablero.pieces(chess.KNIGHT, chess.WHITE)]) + sum([-knightstable[chess.square_mirror(i)] for i in tablero.pieces(chess.KNIGHT, chess.BLACK)])
        alfilPos = sum([bishopstable[i] for i in tablero.pieces(chess.BISHOP, chess.WHITE)]) + sum([-bishopstable[chess.square_mirror(i)] for i in tablero.pieces(chess.BISHOP, chess.BLACK)])
        torrePos = sum([rookstable[i] for i in tablero.pieces(chess.ROOK, chess.WHITE)]) + sum([-rookstable[chess.square_mirror(i)] for i in tablero.pieces(chess.ROOK, chess.BLACK)])
        reinaPos = sum([queenstable[i] for i in tablero.pieces(chess.QUEEN, chess.WHITE)]) + sum([-queenstable[chess.square_mirror(i)] for i in tablero.pieces(chess.QUEEN, chess.BLACK)])
        reyPos = sum([kingstable[i] for i in tablero.pieces(chess.KING, chess.WHITE)]) + sum([-kingstable[chess.square_mirror(i)] for i in tablero.pieces(chess.KING, chess.BLACK)])
    
        valorEval = valorMaterial + peonPos + caballoPos + alfilPos + torrePos + reinaPos + reyPos
    #Esto lo hago porque lo bueno para mí es malo para mi oponente
        if tablero.turn:
            return valorEval
        else:
            return -valorEval

def negamax(tablero, alfa, beta, profundidad):
    maxEval = -999999
    if profundidad == 0 or not tablero.is_game_over():
        return evaluar(tablero)
    for movida in tablero.legal_moves:
        tablero.push(movida)
        valorEval = -(negamax(tablero, -beta, -alfa, profundidad-1))
        maxEval = max(maxEval, valorEval)
        alfa = max(alfa, valorEval)
        if alfa >= beta:
            break
    return maxEval
    
def mejorMovimiento(tablero, profundidad):
    mejorMovimiento = chess.Move.null() #Solo pasó el turno al otro jugador
    maxEval = -999999
    alfa = -999999
    beta = 999999
    for movimiento in tablero.legal_moves:
        tablero.push(movimiento)
        valorEval = -(negamax(tablero, -beta, -alfa, profundidad-1))
        if valorEval > maxEval:
            maxEval = valorEval
            mejorMovimiento = movimiento
        alfa = max(valorEval, alfa)
        tablero.pop()
    return mejorMovimiento

def main():
    tablero = chess.Board()
    while not tablero.is_game_over():
    #for i in range(16):
        #imprimeTablero(tablero)
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
            #movida = mejorMovimiento(tablero, 1)
            tablero.push(movida)
            #print("las blancas movieron", movida)
        else:
            #movida = random.choice([movida for movida in tablero.legal_moves])
            movida = mejorMovimiento(tablero, 7)
            tablero.push(movida)
            #print("las negras movieron", movida)
    #imprimeTablero(tablero)
    return tablero.result()


if __name__ == "__main__":
    empates = 0 #1/2-1/2
    blancas = 0 #1-0
    negras = 0  #0-1
    for i in range(100):
        resultado = main()
        if resultado == "0-1":
            negras += 1
        elif resultado == "1-0":
            blancas += 1
        else: 
            empates += 1
    print("Las blancas ganaron:", blancas)
    print("Las negras ganaron:", negras)
    print("Empates", empates)