from IA import heuristicas as h
import chess
import chess.polyglot
import random
import time


class Juego(object):

    def __init__(self):
        self.tablero = chess.Board()
        self.tablero.castling_rights=False


    """Funciones que aplican para todos los niveles"""

    def imprimetablero(self):
        texto = ""
        texto += "8|"
        texto += self.obtenFila(56, 64)
        texto += "7|"
        texto += self.obtenFila(48, 56)
        texto += "6|"
        texto += self.obtenFila(40, 48)
        texto += "5|"
        texto += self.obtenFila(32, 40)
        texto += "4|"
        texto += self.obtenFila(24, 32)
        texto += "3|"
        texto += self.obtenFila(16, 24)
        texto += "2|"
        texto += self.obtenFila(8, 16)
        texto += "1|"
        texto += self.obtenFila(0, 8)
        texto += "  - - - - - - - -\n"
        texto += "  a b c d e f g h"
        print(texto)

    def obtenFila(self, comienzo, final):
        fila = ""
        for i in range(comienzo, final):
            if self.tablero.piece_at(i) == None:
                fila += ". "
            else:
                fila += str(self.tablero.piece_at(i))+" "
        fila += "\n"
        return fila

    def darJugada(self, ins):
        # while True:
        #ins = input("Da la movida que quieras hacer con el formato a1a2\n")
        try:
            movida = chess.Move(chess.parse_square(
                ins[0:2]), chess.parse_square(ins[2:4]))
            if movida in self.tablero.legal_moves:
                return movida
            else:
                raise Exception
        except:
            #print("Jugada inválida")
            return "Jugada invalida"

    def darJugadaParam(self, move):
        try:
            movida = chess.Move(chess.parse_square(
                move[0:2]), chess.parse_square(move[2:4]))
            if movida in self.tablero.legal_moves:
                return movida
            else:
                raise Exception
        except:
            return "Jugada inválida"

    def seleccionaMovimiento(self, juego, nivel):
        if not juego.tablero.is_game_over():
            if nivel == 0:
                return {
                    "GameOver": False,
                    "move": self.mejorMovimiento0()
                }
            elif nivel == 1:
                return {
                    "GameOver": False,
                    "move": self.mejorMovimiento1(3)
                }
                # return self.mejorMovimiento1(3)
            # elif nivel == -1:
            #     return self.darJugadaParam()
            else:
                return {
                    "GameOver": False,
                    "move": self.mejorMovimiento2(3)
                }
                # return self.mejorMovimiento2(3)
        else:
            return {
                "GameOver": True,
            }

    def obtenPiezas(self):
        piezas = dict()
        piezas["peonB"] = len(self.tablero.pieces(chess.PAWN, chess.WHITE))
        piezas["peonN"] = len(self.tablero.pieces(chess.PAWN, chess.BLACK))
        piezas["caballoB"] = len(self.tablero.pieces(chess.KNIGHT, chess.WHITE))
        piezas["caballoN"] = len(self.tablero.pieces(chess.KNIGHT, chess.BLACK))
        piezas["alfilB"] = len(self.tablero.pieces(chess.BISHOP, chess.WHITE))
        piezas["alfilN"] = len(self.tablero.pieces(chess.BISHOP, chess.BLACK))
        piezas["torreB"] = len(self.tablero.pieces(chess.ROOK, chess.WHITE))
        piezas["torreN"] = len(self.tablero.pieces(chess.ROOK, chess.BLACK))
        piezas["reinaB"] = len(self.tablero.pieces(chess.QUEEN, chess.WHITE))
        piezas["reinaN"] = len(self.tablero.pieces(chess.QUEEN, chess.BLACK))
        return piezas

    """Funciones que aplican para el nivel 0"""

    def mejorMovimiento0(self):
        return random.choice([movida for movida in self.tablero.legal_moves])

    """Funciones que aplican para el nivel 1"""
    def evaluar1(self, numPiezas):
        if self.tablero.is_checkmate():
            if self.tablero.turn:
                return -9999
            else:
                return 9999
        elif self.tablero.is_stalemate():
            return 0
        elif self.tablero.is_insufficient_material():
            return 0
        else:

            valorMaterial = 100 * (numPiezas["peonB"] - numPiezas["peonN"]) 
            + 320 * (numPiezas["caballoB"] - numPiezas["caballoN"]) 
            + 330 * (numPiezas["alfilB"] - numPiezas["alfilN"]) 
            + 500 * (numPiezas["torreB"] - numPiezas["torreN"]) 
            + 900 * (numPiezas["reinaB"] - numPiezas["reinaN"]) 

            peonPos = sum([h.pawntable[i] for i in self.tablero.pieces(chess.PAWN, chess.WHITE)]) + sum([-h.pawntable[chess.square_mirror(i)] for i in self.tablero.pieces(chess.PAWN, chess.BLACK)])
            caballoPos = sum([h.knightstable[i] for i in self.tablero.pieces(chess.KNIGHT, chess.WHITE)]) + sum([-h.knightstable[chess.square_mirror(i)] for i in self.tablero.pieces(chess.KNIGHT, chess.BLACK)])
            alfilPos = sum([h.bishopstable[i] for i in self.tablero.pieces(chess.BISHOP, chess.WHITE)]) + sum([-h.bishopstable[chess.square_mirror(i)] for i in self.tablero.pieces(chess.BISHOP, chess.BLACK)])
            torrePos = sum([h.rookstable[i] for i in self.tablero.pieces(chess.ROOK, chess.WHITE)]) + sum([-h.rookstable[chess.square_mirror(i)] for i in self.tablero.pieces(chess.ROOK, chess.BLACK)])
            reinaPos = sum([h.queenstable[i] for i in self.tablero.pieces(chess.QUEEN, chess.WHITE)]) + sum([-h.queenstable[chess.square_mirror(i)] for i in self.tablero.pieces(chess.QUEEN, chess.BLACK)])
            reyPos = sum([h.kingstable[i] for i in self.tablero.pieces(chess.KING, chess.WHITE)]) + sum([-h.kingstable[chess.square_mirror(i)] for i in self.tablero.pieces(chess.KING, chess.BLACK)])
        
            valorEval = valorMaterial + peonPos + caballoPos + alfilPos + torrePos + reinaPos + reyPos
        #Esto lo hago porque lo bueno para mí es malo para mi oponente
            if self.tablero.turn:
                return valorEval
            else:
                return -valorEval

    def negamax1(self, alfa, beta, profundidad):
        maxEval = -999999
        if profundidad == 0:
            numPiezas = self.obtenPiezas()
            return self.evaluar1(numPiezas)
        for movida in self.tablero.legal_moves:
            self.tablero.push(movida)
            valorEval = -(self.negamax1(-beta, -alfa, profundidad-1))
            self.tablero.pop()
            maxEval = max(maxEval, valorEval)
            alfa = max(alfa, valorEval)
            if alfa >= beta:
                break
        return maxEval

    def mejorMovimiento1(self, profundidad):
        mejorMovimiento = chess.Move.null()  # Solo pasó el turno al otro jugador
        maxEval = -999999
        alfa = -999999
        beta = 999999
        for movimiento in self.tablero.legal_moves:
            self.tablero.push(movimiento)
            valorEval = -(self.negamax1(-beta, -alfa, profundidad-1))
            if valorEval > maxEval:
                maxEval = valorEval
                mejorMovimiento = movimiento
            alfa = max(valorEval, alfa)
            self.tablero.pop()
        return mejorMovimiento
    """Funciones que aplican para el nivel 2"""

    def evaluar2(self):
        if self.tablero.is_checkmate():
            if self.tablero.turn:
                return -9999
            else:
                return 9999
        elif self.tablero.is_stalemate():
            return 0
        elif self.tablero.is_insufficient_material():
            return 0
        else:
            numPiezas = self.obtenPiezas()
            fase = self.calculaFase(numPiezas)
            return ((self.valorMid(numPiezas) * (256 - fase)) + (self.valorEnd(numPiezas) * fase)) / 256;

    def valorMid(self,numPiezas): #Uso diferentes valores materiales y de tablas

        valorMaterial = 82 * (numPiezas["peonB"] - numPiezas["peonN"]) 
        + 337 * (numPiezas["caballoB"] - numPiezas["caballoN"]) 
        + 365 * (numPiezas["alfilB"] - numPiezas["alfilN"]) 
        + 477 * (numPiezas["torreB"] - numPiezas["torreN"]) 
        + 1025 * (numPiezas["reinaB"] - numPiezas["reinaN"]) 

        peonPos = sum([h.mg_pawn_table[chess.square_mirror(i)] for i in self.tablero.pieces(chess.PAWN, chess.WHITE)]) + sum([-h.mg_pawn_table[i] for i in self.tablero.pieces(chess.PAWN, chess.BLACK)])
        caballoPos = sum([h.mg_knight_table[chess.square_mirror(i)] for i in self.tablero.pieces(chess.KNIGHT, chess.WHITE)]) + sum([-h.mg_knight_table[i] for i in self.tablero.pieces(chess.KNIGHT, chess.BLACK)])
        alfilPos = sum([h.mg_bishop_table[chess.square_mirror(i)] for i in self.tablero.pieces(chess.BISHOP, chess.WHITE)]) + sum([-h.mg_bishop_table[i] for i in self.tablero.pieces(chess.BISHOP, chess.BLACK)])
        torrePos = sum([h.mg_rook_table[chess.square_mirror(i)] for i in self.tablero.pieces(chess.ROOK, chess.WHITE)]) + sum([-h.mg_rook_table[i] for i in self.tablero.pieces(chess.ROOK, chess.BLACK)])
        reinaPos = sum([h.mg_queen_table[chess.square_mirror(i)] for i in self.tablero.pieces(chess.QUEEN, chess.WHITE)]) + sum([-h.mg_queen_table[i] for i in self.tablero.pieces(chess.QUEEN, chess.BLACK)])
        reyPos = sum([h.mg_king_table[chess.square_mirror(i)] for i in self.tablero.pieces(chess.KING, chess.WHITE)]) + sum([-h.mg_king_table[i] for i in self.tablero.pieces(chess.KING, chess.BLACK)])

        valorEval = valorMaterial + peonPos + caballoPos + alfilPos + torrePos + reinaPos + reyPos
        #Esto lo hago porque lo bueno para mí es malo para mi oponente
        if self.tablero.turn:
            return valorEval
        else:
            return -valorEval


    def valorEnd(self, numPiezas): #Uso diferentes valores materiales y de tablas
        valorMaterial = 94 * (numPiezas["peonB"] - numPiezas["peonN"]) 
        + 281 * (numPiezas["caballoB"] - numPiezas["caballoN"]) 
        + 297 * (numPiezas["alfilB"] - numPiezas["alfilN"]) 
        + 512 * (numPiezas["torreB"] - numPiezas["torreN"]) 
        + 936 * (numPiezas["reinaB"] - numPiezas["reinaN"]) 
        
        peonPos = sum([h.eg_pawn_table[chess.square_mirror(i)] for i in self.tablero.pieces(chess.PAWN, chess.WHITE)]) + sum([-h.eg_pawn_table[i] for i in self.tablero.pieces(chess.PAWN, chess.BLACK)])
        caballoPos = sum([h.eg_knight_table[chess.square_mirror(i)] for i in self.tablero.pieces(chess.KNIGHT, chess.WHITE)]) + sum([-h.eg_knight_table[i] for i in self.tablero.pieces(chess.KNIGHT, chess.BLACK)])
        alfilPos = sum([h.eg_bishop_table[chess.square_mirror(i)] for i in self.tablero.pieces(chess.BISHOP, chess.WHITE)]) + sum([-h.eg_bishop_table[i] for i in self.tablero.pieces(chess.BISHOP, chess.BLACK)])
        torrePos = sum([h.eg_rook_table[chess.square_mirror(i)] for i in self.tablero.pieces(chess.ROOK, chess.WHITE)]) + sum([-h.eg_rook_table[i] for i in self.tablero.pieces(chess.ROOK, chess.BLACK)])
        reinaPos = sum([h.eg_queen_table[chess.square_mirror(i)] for i in self.tablero.pieces(chess.QUEEN, chess.WHITE)]) + sum([-h.eg_queen_table[i] for i in self.tablero.pieces(chess.QUEEN, chess.BLACK)])
        reyPos = sum([h.eg_king_table[chess.square_mirror(i)] for i in self.tablero.pieces(chess.KING, chess.WHITE)]) + sum([-h.eg_king_table[i] for i in self.tablero.pieces(chess.KING, chess.BLACK)])

        valorEval = valorMaterial + peonPos + caballoPos + alfilPos + torrePos + reinaPos + reyPos
        #Esto lo hago porque lo bueno para mí es malo para mi oponente
        if self.tablero.turn:
            return valorEval
        else:
            return -valorEval
        
    def calculaFase(self, numPiezas):
        
        fasePeon = 0
        faseCaballo = 1
        faseAlfil = 1
        faseTorre = 2
        faseReina = 4
        faseTotal = fasePeon*16 + faseCaballo*4 
        + faseAlfil*4 + faseTorre*4 + faseReina*2
        fase = faseTotal

        fase -= numPiezas["peonB"] * fasePeon
        fase -= numPiezas["peonN"] * fasePeon
        fase -= numPiezas["caballoB"] * faseCaballo
        fase -= numPiezas["caballoN"] * faseCaballo
        fase -= numPiezas["alfilB"]* faseAlfil
        fase -= numPiezas["alfilN"] * faseAlfil
        fase -= numPiezas["torreB"] * faseTorre
        fase -= numPiezas["torreN"] * faseTorre
        fase -= numPiezas["reinaB"] * faseReina
        fase -= numPiezas["reinaN"] * faseReina
        
        fase = (fase * 256 + (faseTotal/2)) / faseTotal
        return fase

    def quiesce(self, alfa, beta):  # Sigo buscando hasta encontrar una pos quieta
        stand_pat = self.evaluar2()  # Si no hace nada cual es la eval
        if (stand_pat >= beta):  # No va a capturar nada y regresa beta
            return beta

        alfa = max(alfa, stand_pat)

        for movida in self.tablero.legal_moves:
            if self.tablero.is_capture(movida):
                self.tablero.push(movida)
                puntaje = -self.quiesce(-beta, -alfa)
                self.tablero.pop()

                if (puntaje >= beta):
                    return beta

                alfa = max(alfa, puntaje)

        return alfa

    def negamax2(self, alfa, beta, profundidad):
        maxEval = -999999
        if profundidad == 0:
            return self.quiesce(alfa, beta)
        for movida in self.tablero.legal_moves:
            self.tablero.push(movida)
            valorEval = -(self.negamax2(-beta, -alfa, profundidad-1))
            self.tablero.pop()
            maxEval = max(maxEval, valorEval)
            alfa = max(alfa, valorEval)
            if alfa >= beta:
                break
        return maxEval

    def mejorMovimiento2(self, profundidad):
        try:
            movida = chess.polyglot.MemoryMappedReader("Performance.bin").weighted_choice(self.tablero).move
            return movida

        except:
            mejorMovimiento = chess.Move.null()  # Solo pasó el turno al otro jugador
            maxEval = -999999
            alfa = -999999
            beta = 999999
            for movimiento in self.tablero.legal_moves:
                self.tablero.push(movimiento)
                valorEval = -(self.negamax2(-beta, -alfa, profundidad-1))
                if valorEval > maxEval:
                    maxEval = valorEval
                    mejorMovimiento = movimiento
                alfa = max(valorEval, alfa)
                self.tablero.pop()
                
        return mejorMovimiento
    """Ejecución del programa"""

    def jugar(self,nivelCompu, nivelHumano, jugadorHumano):
        #self.imprimetablero()
        while not self.tablero.is_game_over():
            if self.tablero.turn == jugadorHumano:  # Blancas
                movida = self.seleccionaMovimiento(nivelHumano)
            else:  # Negras
                movida = self.seleccionaMovimiento(nivelCompu)
            self.tablero.push(movida)
            self.imprimetablero()
        # imprimetablero()
        return self.tablero.result()


# if __name__ == "__main__":
#     empates = 0  # 1/2-1/2
#     blancas = 0  # 1-0
#     negras = 0  # 0-1
#     inicio = time.time()
#     nivelCompu = 2
#     nivelHumano = 0
#     jugadorHumano = True  # True si juega como las blancas, False si juega como las negras
#     for i in range(1):
#         ai = Juego()
#         #ai.tablero = chess.Board()
#         resultado = ai.jugar(nivelCompu, nivelHumano, True)
#         print("Juego:", i+1)
#         if resultado == "0-1":
#             negras += 1
#         elif resultado == "1-0":
#             blancas += 1
#         else:
#             empates += 1
#     print("--- %s segundos ---" % (time.time() - inicio))
#     print("Las blancas ganaron:", blancas)
#     print("Las negras ganaron:", negras)
#     print("Empates", empates)
