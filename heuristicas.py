"""Rey = No tiene valor, pues no se puede capturar, pero necesito un valor para la heuristica
Reina = 9
Alfil = 3.25 (Según Bobby Fischer y Kasparov)
Caballo = 3
Peón = 1
Torre = 5"""


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
