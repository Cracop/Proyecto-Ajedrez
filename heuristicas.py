"""Rey = No tiene valor, pues no se puede capturar, pero necesito un valor para la heuristica
Reina = 9
Alfil = 3.25 (Según Bobby Fischer y Kasparov)
Caballo = 3
Peón = 1
Torre = 5"""
#Modificar los valores, multiplicarlos por 10, o 100. Como veamos

def heuristicaMaterial(blancas, negras):
    # solo sumo los valores de las piezas
    valores = {
        "Peon": 1,
        "Torre": 5,
        "Caballo": 3,
        "Alfil": 3.25,
        "Dama": 9,
        "Rey": 20
    }
    valorBlancas = 0
    for pb in blancas.values():
        valorBlancas += valores[pb.tipo]
    valorNegras = 0
    for pn in negras.values():
        valorNegras += valores[pn.tipo]
    return valorBlancas - valorNegras

# Agregar las tablas con los valores por pieza/posición
#Se trata de valores por piezas
#Decidir si usar un numpy array o un array normal
#Depende de como calcule el movimiento y si voy a seguir guardando las piezas 
#   en el diccionario como lo hago ahora
peonValores = [
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 5, 10, 10,-20,-20, 10, 10,  5],
        [ 5, -5,-10,  0,  0,-10, -5,  5],
        [ 0,  0,  0, 20, 20,  0,  0,  0],
        [ 5,  5, 10, 25, 25, 10,  5,  5],
        [10, 10, 20, 30, 30, 20, 10, 10],
        [50, 50, 50, 50, 50, 50, 50, 50],
        [ 0,  0,  0,  0,  0,  0,  0,  0]
    ]

caballoValores = [
    [-50, -40, -30, -30, -30, -30, -40, -50],
    [-40, -20,   0,   5,   5,   0, -20, -40],
    [-30,   5,  10,  15,  15,  10,   5, -30],
    [-30,   0,  15,  20,  20,  15,   0, -30],
    [-30,   5,  15,  20,  20,  15,   0, -30],
    [-30,   0,  10,  15,  15,  10,   0, -30],
    [-40, -20,   0,   0,   0,   0, -20, -40],
    [-50, -40, -30, -30, -30, -30, -40, -50]
]

alfilValores = [
    [-20, -10, -10, -10, -10, -10, -10, -20],
    [-10,   5,   0,   0,   0,   0,   5, -10],
    [-10,  10,  10,  10,  10,  10,  10, -10],
    [-10,   0,  10,  10,  10,  10,   0, -10],
    [-10,   5,   5,  10,  10,   5,   5, -10],
    [-10,   0,   5,  10,  10,   5,   0, -10],
    [-10,   0,   0,   0,   0,   0,   0, -10],
    [-20, -10, -10, -10, -10, -10, -10, -20]
]

torreValores = [
    [ 0,  0,  0,  5,  5,  0,  0,  0],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [ 5, 10, 10, 10, 10, 10, 10,  5],
    [ 0,  0,  0,  0,  0,  0,  0,  0]
]

damaValores = [
    [-20, -10, -10, -5, -5, -10, -10, -20],
    [-10,   0,   5,  0,  0,   0,   0, -10],
    [-10,   5,   5,  5,  5,   5,   0, -10],
    [  0,   0,   5,  5,  5,   5,   0,  -5],
    [ -5,   0,   5,  5,  5,   5,   0,  -5],
    [-10,   0,   5,  5,  5,   5,   0, -10],
    [-10,   0,   0,  0,  0,   0,   0, -10],
    [-20, -10, -10, -5, -5, -10, -10, -20]
]

def heuristicaPosiciones(color):
    alfiles = valorPorPieza(color, "Alfil", alfilValores)
    peones = valorPorPieza(color, "Peon", peonValores)
    caballos = valorPorPieza(color, "Caballo", caballoValores)
    torres = valorPorPieza(color, "Torre", torreValores)
    dama = valorPorPieza(color, "Dama", damaValores)
    return alfiles + peones + caballos + torres + dama
    

def valorPorPieza(color, tipo, valores):
    valorPieza = 0
    for pos, pieza in color.items():
        if pieza.tipo == tipo:
            valorPieza += valores[int(pos/8)][pos % 8]
    return valorPieza