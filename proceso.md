# Proceso de la creación de una IA capaz de jugar ajedrez contra un humano
## Guía sobre como funciona la librería de Chess
Se hizo con el objetivo de poder implenetarla de manera correcta.

### Liberías importadas
- chess
- random

### Creación del tablero
Se utiliza `tablero = chess.Board()` para crear un tablero, el parametro que se le pasa es la [Notación FEN](https://en.wikipedia.org/wiki/Forsyth–Edwards_Notation) del estado del tablero que queremos:
- Si no se le pasa nada, por default te crea el tablero en su estado inicial
- Si se le pasa `None` se crea un tablero vacío

### Implementación del tablero
Analizando el código de la librería nos dimos cuenta que los cuadros del tablero están definido por un número que va del 0 al 63.
```
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
```
Algo que se debe notar, según las reglas del ajedrez, jugando como las blancas, el recuadro a1 debe ubicarse en la esquina inferior izquierda, por lo que esta implementación está invertida verticalmente.

#### Piezas
- P/p = peon
- N/n = caballo
- B/b = alfil
- Q/q = Dama
- K/k = Rey
- R/r = Torre

##### Colores de las piezas
El color de una pieza se guarda como un Booleano, donde:
- `True` si la pieza es blanca
- `False` si la pieza es negra

### Impresión del Tablero
Pata poder visualizar el tablero en la terminal se puede hacer de dos maneras:
- Con una función de la librería
- Con un par de funciónes programada por nosotros

#### Función de la libería
De esta forma solo tenemos que escribir `print(tablero)` lo cual nos dará lo siguiente:
```
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
```
Donde las mayúsculas son las piezas blancas y las minúsculas son las negras.
Se puede notar que no nos da las coordenadas

#### Nuestras funciones 
Sean nuestras funciones las siguientes:
```
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
```
Lo cual nos regresa:
```
8 r n b q k b n r 
7 p p p p p p p p 
6 . . . . . . . . 
5 . . . . . . . . 
4 . . . . . . . . 
3 . . . . . . . . 
2 P P P P P P P P 
1 R N B Q K B N R 
  a b c d e f g h
```
Nos podemos dar cuenta como es que el tablero está invertido en cuanto a los número y que ahora ya tenemos las coordenadas para facilitarnos la vida.

###Notación de los cuadros
Nótese que si bien la manera en la que esta guardado el código es con números del 0 al 63, ajedrez se juega utilizando coordenadas. 
- Las filas se denotan con números del `1` al `8`.
- Las columnas se denotan con letras de la `a` a la `h`.

Por lo tanto tenemos que encontrar una forma de pasar de coordenadas a números. Por suerte la librería tiene ciertas funciones que nos permiten pasar de uno a otro:
- Con `chess.square_name(0)` me regresa sus coordenadas, en este caso `a1`
- `chess.parse_square("a1")` me regresa su número, en este caso `0`