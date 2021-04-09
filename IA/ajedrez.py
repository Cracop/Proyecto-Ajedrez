import heuristicas as h
import chess
import chess.polyglot
import random
import time

"""Funciones que aplican para todos los niveles"""
def imprimeTablero():
    texto=""
    texto += "8|"
    texto+=obtenFila(56,64)
    texto += "7|"
    texto+=obtenFila(48,56)
    texto += "6|"
    texto+=obtenFila(40,48)
    texto += "5|"
    texto+=obtenFila(32,40)
    texto += "4|"
    texto+=obtenFila(24,32)
    texto += "3|"
    texto+=obtenFila(16,24)
    texto += "2|"
    texto+=obtenFila(8,16)
    texto += "1|"
    texto+=obtenFila(0,8) 
    texto += "  - - - - - - - -\n"
    texto += "  a b c d e f g h"
    print(texto)

def obtenFila(comienzo, final):
    fila = ""
    for i in range(comienzo, final):
        if tablero.piece_at(i) == None:
            fila+=". "
        else:
            fila+=str(tablero.piece_at(i))+" "
    fila+="\n"
    return fila

def darJugada():
    while True:
        ins = input("Da la movida que quieras hacer con el formato a1a2\n")
        try:
            movida = chess.Move(chess.parse_square(ins[0:2]),chess.parse_square(ins[2:4]))
            if movida in tablero.legal_moves:
                return movida
            else: 
                raise Exception
        except:
            print("Jugada inválida")

def seleccionaMovimiento(nivel):
    if nivel == 0:
        return mejorMovimiento0()
    elif nivel == 1:
        return mejorMovimiento1(3)
    elif nivel == -1:
        return darJugada()
    else:
        return mejorMovimiento2(3)

"""Funciones que aplican para el nivel 0"""
def mejorMovimiento0():
    return  random.choice([movida for movida in tablero.legal_moves])

"""Funciones que aplican para el nivel 1"""
def evaluar1():
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

        peonPos = sum([h.pawntable[i] for i in tablero.pieces(chess.PAWN, chess.WHITE)]) + sum([-h.pawntable[chess.square_mirror(i)] for i in tablero.pieces(chess.PAWN, chess.BLACK)])
        caballoPos = sum([h.knightstable[i] for i in tablero.pieces(chess.KNIGHT, chess.WHITE)]) + sum([-h.knightstable[chess.square_mirror(i)] for i in tablero.pieces(chess.KNIGHT, chess.BLACK)])
        alfilPos = sum([h.bishopstable[i] for i in tablero.pieces(chess.BISHOP, chess.WHITE)]) + sum([-h.bishopstable[chess.square_mirror(i)] for i in tablero.pieces(chess.BISHOP, chess.BLACK)])
        torrePos = sum([h.rookstable[i] for i in tablero.pieces(chess.ROOK, chess.WHITE)]) + sum([-h.rookstable[chess.square_mirror(i)] for i in tablero.pieces(chess.ROOK, chess.BLACK)])
        reinaPos = sum([h.queenstable[i] for i in tablero.pieces(chess.QUEEN, chess.WHITE)]) + sum([-h.queenstable[chess.square_mirror(i)] for i in tablero.pieces(chess.QUEEN, chess.BLACK)])
        reyPos = sum([h.kingstable[i] for i in tablero.pieces(chess.KING, chess.WHITE)]) + sum([-h.kingstable[chess.square_mirror(i)] for i in tablero.pieces(chess.KING, chess.BLACK)])
    
        valorEval = valorMaterial + peonPos + caballoPos + alfilPos + torrePos + reinaPos + reyPos
    #Esto lo hago porque lo bueno para mí es malo para mi oponente
        if tablero.turn:
            return valorEval
        else:
            return -valorEval

def negamax1(alfa, beta, profundidad):
    maxEval = -999999
    if profundidad == 0:
        return evaluar1()
    for movida in tablero.legal_moves:
        tablero.push(movida)
        valorEval = -(negamax1(-beta, -alfa, profundidad-1))
        tablero.pop()
        maxEval = max(maxEval, valorEval)
        alfa = max(alfa, valorEval)
        if alfa >= beta:
            break
    return maxEval

def mejorMovimiento1(profundidad):
    mejorMovimiento = chess.Move.null() #Solo pasó el turno al otro jugador
    maxEval = -999999
    alfa = -999999
    beta = 999999
    for movimiento in tablero.legal_moves:
        tablero.push(movimiento)
        valorEval = -(negamax1(-beta, -alfa, profundidad-1))
        if valorEval > maxEval:
            maxEval = valorEval
            mejorMovimiento = movimiento
        alfa = max(valorEval, alfa)
        tablero.pop()
    return mejorMovimiento
"""Funciones que aplican para el nivel 2"""
def evaluar2():
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
        fase = calculaFase()
        return ((valorMid() * (256 - fase)) + (valorEnd() * fase)) / 256;

def valorMid(): #Uso diferentes valores materiales y de tablas
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

    valorMaterial = 82 * (peonB - peonN) + 337 * (caballoB - caballoN) + 365 * (alfilB - alfilN) + 477 * (torreB - torreN) + 1025 * (reinaB - reinaN)

    peonPos = sum([h.mg_pawn_table[chess.square_mirror(i)] for i in tablero.pieces(chess.PAWN, chess.WHITE)]) + sum([-h.mg_pawn_table[i] for i in tablero.pieces(chess.PAWN, chess.BLACK)])
    caballoPos = sum([h.mg_knight_table[chess.square_mirror(i)] for i in tablero.pieces(chess.KNIGHT, chess.WHITE)]) + sum([-h.mg_knight_table[i] for i in tablero.pieces(chess.KNIGHT, chess.BLACK)])
    alfilPos = sum([h.mg_bishop_table[chess.square_mirror(i)] for i in tablero.pieces(chess.BISHOP, chess.WHITE)]) + sum([-h.mg_bishop_table[i] for i in tablero.pieces(chess.BISHOP, chess.BLACK)])
    torrePos = sum([h.mg_rook_table[chess.square_mirror(i)] for i in tablero.pieces(chess.ROOK, chess.WHITE)]) + sum([-h.mg_rook_table[i] for i in tablero.pieces(chess.ROOK, chess.BLACK)])
    reinaPos = sum([h.mg_queen_table[chess.square_mirror(i)] for i in tablero.pieces(chess.QUEEN, chess.WHITE)]) + sum([-h.mg_queen_table[i] for i in tablero.pieces(chess.QUEEN, chess.BLACK)])
    reyPos = sum([h.mg_king_table[chess.square_mirror(i)] for i in tablero.pieces(chess.KING, chess.WHITE)]) + sum([-h.mg_king_table[i] for i in tablero.pieces(chess.KING, chess.BLACK)])

    valorEval = valorMaterial + peonPos + caballoPos + alfilPos + torrePos + reinaPos + reyPos
    #Esto lo hago porque lo bueno para mí es malo para mi oponente
    if tablero.turn:
        return valorEval
    else:
        return -valorEval


def valorEnd(): #Uso diferentes valores materiales y de tablas
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
    
    valorMaterial = 94 * (peonB - peonN) + 281 * (caballoB - caballoN) + 297 * (alfilB - alfilN) + 512 * (torreB - torreN) + 936 * (reinaB - reinaN) 
    
    peonPos = sum([h.eg_pawn_table[chess.square_mirror(i)] for i in tablero.pieces(chess.PAWN, chess.WHITE)]) + sum([-h.eg_pawn_table[i] for i in tablero.pieces(chess.PAWN, chess.BLACK)])
    caballoPos = sum([h.eg_knight_table[chess.square_mirror(i)] for i in tablero.pieces(chess.KNIGHT, chess.WHITE)]) + sum([-h.eg_knight_table[i] for i in tablero.pieces(chess.KNIGHT, chess.BLACK)])
    alfilPos = sum([h.eg_bishop_table[chess.square_mirror(i)] for i in tablero.pieces(chess.BISHOP, chess.WHITE)]) + sum([-h.eg_bishop_table[i] for i in tablero.pieces(chess.BISHOP, chess.BLACK)])
    torrePos = sum([h.eg_rook_table[chess.square_mirror(i)] for i in tablero.pieces(chess.ROOK, chess.WHITE)]) + sum([-h.eg_rook_table[i] for i in tablero.pieces(chess.ROOK, chess.BLACK)])
    reinaPos = sum([h.eg_queen_table[chess.square_mirror(i)] for i in tablero.pieces(chess.QUEEN, chess.WHITE)]) + sum([-h.eg_queen_table[i] for i in tablero.pieces(chess.QUEEN, chess.BLACK)])
    reyPos = sum([h.eg_king_table[chess.square_mirror(i)] for i in tablero.pieces(chess.KING, chess.WHITE)]) + sum([-h.eg_king_table[i] for i in tablero.pieces(chess.KING, chess.BLACK)])

    valorEval = valorMaterial + peonPos + caballoPos + alfilPos + torrePos + reinaPos + reyPos
    #Esto lo hago porque lo bueno para mí es malo para mi oponente
    if tablero.turn:
        return valorEval
    else:
        return -valorEval
    


def calculaFase():
    fasePeon = 0
    faseCaballo = 1
    faseAlfil = 1
    faseTorre = 2
    faseReina = 4
    faseTotal = fasePeon*16 + faseCaballo*4 + faseAlfil*4 + faseTorre*4 + faseReina*2
    fase = faseTotal

    fase -= len(tablero.pieces(chess.PAWN, chess.WHITE)) * fasePeon
    fase -= len(tablero.pieces(chess.PAWN, chess.BLACK)) * fasePeon
    fase -= len(tablero.pieces(chess.KNIGHT, chess.WHITE)) * faseCaballo
    fase -= len(tablero.pieces(chess.KNIGHT, chess.BLACK)) * faseCaballo
    fase -= len(tablero.pieces(chess.BISHOP, chess.WHITE)) * faseAlfil
    fase -= len(tablero.pieces(chess.BISHOP, chess.BLACK)) * faseAlfil
    fase -= len(tablero.pieces(chess.ROOK, chess.WHITE)) * faseTorre
    fase -= len(tablero.pieces(chess.ROOK, chess.BLACK)) * faseTorre
    fase -= len(tablero.pieces(chess.QUEEN, chess.WHITE)) * faseReina
    fase -= len(tablero.pieces(chess.QUEEN, chess.BLACK)) * faseReina
    
    fase = (fase * 256 + (faseTotal/2)) / faseTotal
    return fase

def quiesce(alfa, beta): #Sigo buscando hasta encontrar una pos quieta
    stand_pat = evaluar2() #Si no hace nada cual es la eval
    if (stand_pat >= beta):#No va a capturar nada y regresa beta
        return beta

    alfa=max(alfa, stand_pat)

    for movida in tablero.legal_moves:
        if tablero.is_capture(movida):
            tablero.push(movida)
            puntaje = -quiesce(-beta, -alfa)
            tablero.pop()

            if (puntaje >= beta):
                return beta

            alfa=max(alfa, puntaje)
            
    return alfa

def negamax2(alfa, beta, profundidad):
    maxEval = -999999
    if profundidad == 0:
        return quiesce(alfa, beta)
    for movida in tablero.legal_moves:
        tablero.push(movida)
        valorEval = -(negamax2(-beta, -alfa, profundidad-1))
        tablero.pop()
        maxEval = max(maxEval, valorEval)
        alfa = max(alfa, valorEval)
        if alfa >= beta:
            break
    return maxEval

def mejorMovimiento2(profundidad):
    try:
        movida = chess.polyglot.MemoryMappedReader("Perfect2017-LC0.bin").weighted_choice(tablero).move
        return movida

    except:
        mejorMovimiento = chess.Move.null() #Solo pasó el turno al otro jugador
        maxEval = -999999
        alfa = -999999
        beta = 999999
        for movimiento in tablero.legal_moves:
            tablero.push(movimiento)
            valorEval = -(negamax2(-beta, -alfa, profundidad-1))
            if valorEval > maxEval:
                maxEval = valorEval
                mejorMovimiento = movimiento
            alfa = max(valorEval, alfa)
            tablero.pop()
    return mejorMovimiento
"""Ejecución del programa"""

def main(nivelCompu, nivelHumano, jugadorHumano):
    #imprimeTablero()
    while not tablero.is_game_over():
        if tablero.turn == jugadorHumano: #Blancas
            movida = seleccionaMovimiento(nivelHumano)
        else: #Negras
            movida = seleccionaMovimiento(nivelCompu)
        tablero.push(movida)
     #   imprimeTablero()
    #imprimeTablero()
    return tablero.result()




if __name__ == "__main__":
    #tablero = chess.Board() 
    empates = 0 #1/2-1/2
    blancas = 0 #1-0
    negras = 0  #0-1
    start_time = time.time()    
    nivelCompu = 2
    nivelHumano = 0
    jugadorHumano = True #True si juega como las blancas, False si juega como las negras    
    for i in range(10):
        tablero = chess.Board()
        resultado = main(nivelCompu, nivelHumano, jugadorHumano)
        print("Juego:",i)
        if resultado == "0-1":
            negras += 1
        elif resultado == "1-0":
            blancas += 1
        else: 
            empates += 1
    print("--- %s seconds ---" % (time.time() - start_time))
    #print(prueba)
    print("Las blancas ganaron:", blancas)
    print("Las negras ganaron:", negras)
    print("Empates", empates)
