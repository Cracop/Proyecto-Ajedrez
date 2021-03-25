# Proceso de la creación de una IA capaz de jugar ajedrez contra un humano
## Guía sobre como funciona la librería de Chess
Se hizo con el objetivo de poder implenetarla de manera correcta.

### Liberías importadas
    -chess
    -random

### Creación del tablero
Se utiliza 'tablero = chess.Board()' para crear un tablero, el parametro que se le pasa es la notación FEN del estado del tablero que queremos.
    -Si no se le pasa nada, por default te crea el tablero en su estado inicial.
    -Si se le pasa 'None' se crea un tablero vacío.

### Implementación del tablero
Analizando el código de la librería nos dimos cuenta que los cuadros del tablero están definido por un número que va del 0 al 63.
'''
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
'''
Algo que se debe notar, según las reglas del ajedrez, jugando como las blancas, el recuadro a1 debe ubicarse en la esquina inferior izquierda, por lo que esta implementación está invertida verticalmente.

### Impresión del Tablero
Pata poder visualizar el tablero en la terminal se puede hacer de dos maneras:
    - Con una función de la librería
    - Con un par de funciónes programada por nosotros
    
#### Función de la libería
