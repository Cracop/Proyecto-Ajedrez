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
(Simbolo|Tipo)
- P/p = peon | 1
- N/n = caballo | 2
- B/b = alfil | 3 
- R/r = Torre | 4
- Q/q = Reina | 5 
- K/k = Rey | 6

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
```
Lo cual nos regresa:
```
8|r n b q k b n r 
7|p p p p p p p p 
6|. . . . . . . . 
5|. . . . . . . . 
4|. . . . . . . . 
3|. . . . . . . . 
2|P P P P P P P P 
1|R N B Q K B N R 
  - - - - - - - -
  a b c d e f g h

```
Nos podemos dar cuenta como es que el tablero está invertido en cuanto a los número y que ahora ya tenemos las coordenadas para facilitarnos la vida.

### Notación de los cuadros
Nótese que si bien la manera en la que esta guardado el código es con números del 0 al 63, ajedrez se juega utilizando coordenadas. 
- Las filas se denotan con números del `1` al `8`.
- Las columnas se denotan con letras de la `a` a la `h`.

Por lo tanto tenemos que encontrar una forma de pasar de coordenadas a números. Por suerte la librería tiene ciertas funciones que nos permiten pasar de uno a otro:
- Con `chess.square_name(0)` me regresa sus coordenadas, en este caso `a1`
- Con `chess.parse_square("a1")` me regresa su número, en este caso `0`

### Generación de movimientos
Para generar los movimientos utilizamos funciones de la librería, existen dos tipos de movimientos:
- `tablero.legal_moves` te genera todos los movimientos legales en ese estado del tablero de acuerdo al jugador que tiene el turno.
- `tablero.pseudo_legal_moves` la diferencia con los movimientos legales, es que los pseudolegales pueden hacer que el Rey quede en jaque.

Ambos te dan una especie de lista, la cual es iterable pero no indexable. Para casos futuros utilizaremos los movimientos completamente legales. 

Para ver de quién es turno puedo ver una propiedad de `tablero.turn`

Más alla de obtener una lista de movimientos, nosotros podemos dar de manera explicita un movimiento creando un objeto de la clase `Move`
`chess.Move(cuadroInicial, cuadroFinal)`
- ambos cuadros se dan utilizando un número del `0` al `63`
Un ejemplo de la creación de un movimiento sería:
```
movida = chess.Move(1,25)
print(movida)
```
Lo cual nos daría `b1b4`

### Aplicación de Movimientos
El tablero contiene una pila `tablero.move_stack` donde se almacenan todas las movidas, por lo que manipularlo con las siguientes funciones.
- `tablero.push(movida)' para realizar un objeto `Move` que recibe como parametro como el creado anteriormente, automaticamente se cambia el turno.
- `tablero.pop()` regreso el tablero a a como estaba un turno antes.
- `tablero.peek()` puedo ver la ultima movida que se hizo

#### Ejemplos
Con push()
```
print("Turno de", tablero.turn, "\n")
print(tablero, "\n")
movida = chess.Move(1,16)
print("Movida realizada", movida, "\n")
tablero.push(movida)
print("Turno de", tablero.turn , "\n")
print(tablero, "\n")
movida = chess.Move(62,45)
print("Movida realizada", movida, "\n")
tablero.push(movida)
print("Turno de", tablero.turn , "\n")
print(tablero)
```

```
Turno de True 

r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R 

Movida realizada b1a3 

Turno de False 

r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
N . . . . . . .
P P P P P P P P
R . B Q K B N R 

Movida realizada g8f6 

Turno de True 

r n b q k b . r
p p p p p p p p
. . . . . n . .
. . . . . . . .
. . . . . . . .
N . . . . . . .
P P P P P P P P
R . B Q K B N R
```
Ejemplo de pop()
```
print("Turno de", tablero.turn, "\n")
print(tablero, "\n")
movida = chess.Move(1,16)
print("Movida realizada", movida, "\n")
tablero.push(movida)
print("Turno de", tablero.turn , "\n")
print(tablero, "\n")
tablero.pop()
print("Turno de", tablero.turn , "\n")
print(tablero)
```
```
Turno de True 

r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R 

Movida realizada b1a3 

Turno de False 

r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
N . . . . . . .
P P P P P P P P
R . B Q K B N R 

Turno de True 

r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
```
Ejemplo de peek()
```
print("Turno de", tablero.turn, "\n")
print(tablero, "\n")
movida = chess.Move(1,16)
tablero.push(movida)
print("Turno de", tablero.turn , "\n")
print(tablero, "\n")
print("Ultima movida",tablero.peek())
print("Turno de", tablero.turn , "\n")
print(tablero)
```
```
Turno de True 

r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R 

Turno de False 

r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
N . . . . . . .
P P P P P P P P
R . B Q K B N R 

Ultima movida b1a3
Turno de False 

r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
N . . . . . . .
P P P P P P P P
R . B Q K B N R
```
### Aplicación automática de movimientos
Si bien la lista de movimientos no es indexable, si es iterable, por lo que podemos elegir movimientos de manera automática de la lista de movimientos legales.
Un ejemplo de esto es lo siguiente:
```
print(tablero)
for i in range(5):
    movida = random.choice([movida for movida in tablero.legal_moves])
    tablero.push(movida)
    print("")
    print(tablero)
```
Se utiliza `random.choice([movida for movida in tablero.legal_moves]` para elegir un movimiento de manera aleatoria de los posibles movimientos legales para un estado específico del tablero.
Aquí podemos observar los primeros 5 turnos donde los jugadores realizan movimientos de manera aleatoria.
```
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R

r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
N . . . . . . .
P P P P P P P P
R . B Q K B N R

r n b q k b n r
p p p p p . p p
. . . . . p . .
. . . . . . . .
. . . . . . . .
N . . . . . . .
P P P P P P P P
R . B Q K B N R

r n b q k b n r
p p p p p . p p
. . . . . p . .
. . . . . . . .
. . . . . . . .
N . . P . . . .
P P P . P P P P
R . B Q K B N R

r n b q k b n r
. p p p p . p p
p . . . . p . .
. . . . . . . .
. . . . . . . .
N . . P . . . .
P P P . P P P P
R . B Q K B N R

r n b q k b n r
. p p p p . p p
p . . . . p . B
. . . . . . . .
. . . . . . . .
N . . P . . . .
P P P . P P P P
R . . Q K B N R
```
#### Dar jugadas explicitas
Como jugador humano, tengo que poderle dar una movida a jugar al programa, de preferencia mediante las coordenadas y no los números de los cuadros. Igual tengo que tener una manera de comprobar si una jugada es legal. Una fácil implementación de eso es lo siguiente
``` 
imprimeTablero(tablero)
ino=input("Coloca la movida que quieras ")
#ino="a2a3"
movida = chess.Move(chess.parse_square(ino[0:2]),chess.parse_square(ino[2:4]))
if movida in tablero.legal_moves:
    tablero.push(movida)
else: 
    print("Movida inválida")
imprimeTablero(tablero)
```
Ya con esto resolvimos que la movida dada por el usuario sea legal, pues se encuentra en los movimientos legales de ese estado del tablero. Sin embargo el programa todavía puede tronar si el usuario da unas coordenadas que se encuentren fuera del tablero o algo que no tengamos contemplado. Este problema se puede resolver fácilmente con un `try-except`
```
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
```
### Condiciones de Fin de Juego
Se puede checar si han sucedido diversos eventos en el tablero actual:
- `tablero.is_check()` me dice si el jugador en turno se encuentra en jaque
- `tablero.is_checkmate()` me dice si el jugador en turno se encuentra en jaquemate
- `tablero.is_stalemate()` me dice si los jugadores se encuentran en empate
- `tablero.is_insufficient_material()` me dice si los jugadores tienen insuficientes piezas como para llegar a un resultado. 
- `tablero.is_game_over()` me dice si el juego a terminado ya sea por jaquemate, empate o piezas insuficientes.

### Resultados
Para dar el resultado utilizamos `print(tablero.result())`
Te puede regresar diferentes resultados:
- `1-0` si ganan las blancas.
- `0-1` si ganan las negras.
- `1/2-1/2` si hubo empate.
- `*` si está indeterminado i.e. si no ha acabado el juego.

## Desarrollo de la IA
### Paso 1: Un Primer Juego Funcional
Antes de pensar en desarrollar un programa fuera bueno jugando ajedrez, teníamos que estar seguros que sabíamos utilizar la librería para tener un programa con el que pudieramos tener una partida. 

Para resolver ese primer problema, tomamos la decisión de el humano jugaría con las blancas y la computadora con las negras. Los movimientos serían dados por el usuario en forma de texto por medio de la terminal, mientras que la computadora elegiría un movimiento al azar cada vez que fuese su turno. 

Utilizamos nuestras funciones `imprimeTablero()` y `obtenFila()` para poder presentarle al usuario un tablero donde se pudieran ver claramente las coordenadas de cada cuadro.

Además de usar esas dos funciones e importar los modulos de `chess` y `random`, ese código consistió en lo siguiente:
```
def main():
    tablero = chess.Board()
    while not tablero.is_game_over():
        imprimeTablero(tablero)
        #print(tablero.turn)
        if tablero.turn:
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
        else:
            movida = random.choice([movida for movida in tablero.legal_moves])
            tablero.push(movida)
            print("las negras movieron", movida)
    imprimeTablero(tablero)
    print(tablero.result())


if __name__ == "__main__":
    main()
```
El programa fue exitoso, las blancas solo se movían cuando el jugador daba una movida válida. 
Si bien no se terminó ningún juego de manera manual, para probar que las condiciones de finalizar el juego se cumplían, se modificó el código para que ambos jugadores fueran la computadora realizando movimientos aleatorios. El código quedó así:
```
def main():
    tablero = chess.Board()
    while not tablero.is_game_over():
        imprimeTablero(tablero)
        #print(tablero.turn)
        if tablero.turn:
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
```
#### Resultados obtenidos
Como una especie de métrica se llevaro a cabo `100` juegos donde la computadora cumplia los papeles de ambos jugadores llevando a cabo partidas aleatorias en cada turno.
Los resultados obtenidos fueron:
- `9` juegos los ganaron las blancas
- `8` juegos los ganaron las negras
- `83` juegos fueron empates

### Paso 2: Elección de las Heurísticas
Para buscar que tipo de heuristicas aplicar y así decidir en que consistía una buena movida, recurrimos a la página de [chess programming](https://www.chessprogramming.org/Evaluation), donde vienen diferentes maneras de evaluar un tablero. En este caso decidimos utilizar una evaluación dada por [Tomasz Michniewski](https://www.chessprogramming.org/Tomasz_Michniewski):

#### Heurística Material
Es un tipo de evaluación sencilla, pues solo consiste en sumar los valores de tus piezas y restarte los valores de las piezas del oponenete. 
```
Peón - 100
Caballo - 320
Alfil - 330
Torre - 500
Reina - 900
Rey - 20000, a pesar de esto no se puede capturar
```
Es una heurística que se utiliza principalmente, pero en conjunto con otras evaluaciones. La razón de esto es porque si bien esta heurística incentiva la captura de piezas, no toma la posición de las piezas o el control del tablero. 
La otra razón por la cual decidimos utilizar otra función fue porque teniamos la corazonada de que en posiciones donde no se pueden capturar las piezas, se explorarían todas las posibilidades y la poda no tendría mayor efecto. 

#### Heurística Posicional
Esto resuelve el problema anterior, pues así la computadora va a intentar sus piezas de manera que controle el tablero. La manera con la que esto se logra, es que a cada pieza se le asigna un valor dependiendo del cuadro que ocupe en el tablero. Se debe notar que el posicionamiento ideal es diferente para cada tipo de pieza.

##### Posición de Peones

