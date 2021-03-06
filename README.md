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
Así se ven en el tablero (Simbolo|Tipo)
- P/p = peon | 1
- N/n = caballo | 2
- B/b = alfil | 3 
- R/r = Torre | 4
- Q/q = Reina | 5 
- K/k = Rey | 6
Así se guardan en el código
- `chess.PAWN: chess.PieceType = 1`
- `chess.KNIGHT: chess.PieceType = 2`
- `chess.BISHOP: chess.PieceType = 3`
- `chess.ROOK: chess.PieceType = 4`
- `chess.QUEEN: chess.PieceType = 5`
- `chess.KING: chess.PieceType = 6`

##### Colores de las piezas
El color de una pieza se guarda como un Booleano, donde:
- `chess.WHITE: chess.Color = True`
- `chess.BLACK: chess.Color = False`

##### Acceder a las piezas
Puedo acceder a las piezas de diferentes maneras:
print(tablero.pieces(chess.BISHOP, chess.WHITE)) o 

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

Si quiero saber si el movimiento sería una captura, puedo utilizar `tablero.is_capture(movida)`, lo cual me regresa un booleano.

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
Para buscar que tipo de heuristicas aplicar y así decidir en que consistía una buena movida, recurrimos a la página de [chess programming](https://www.chessprogramming.org/Evaluation), donde vienen diferentes maneras de evaluar un tablero. En este caso decidimos utilizar evaluaciones dadas por [Tomasz Michniewski](https://www.chessprogramming.org/Tomasz_Michniewski):

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
Esto resuelve el problema anterior, pues así la computadora va a intentar sus piezas de manera que controle el tablero. La manera con la que esto se logra, es que a cada pieza se le asigna un valor dependiendo del cuadro que ocupe en el tablero. Se debe notar que el posicionamiento ideal es diferente para cada tipo de pieza. En las tablas, si un valor es positivo, entonces la computadora va a intentar poner una pieza ahí.

##### Peones
Su estrategia principal avanzar, de igual manera lo que se trata es evitar que los peones centrales se queden inmóviles.
```
pawntable = [
 0,  0,  0,  0,  0,  0,  0,  0,
 5, 10, 10,-20,-20, 10, 10,  5,
 5, -5,-10,  0,  0,-10, -5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5,  5, 10, 25, 25, 10,  5,  5,
10, 10, 20, 30, 30, 20, 10, 10,
50, 50, 50, 50, 50, 50, 50, 50,
 0,  0,  0,  0,  0,  0,  0,  0]
```
##### Caballo
Mientras se encuentren en el centro es una estrategia válida, estar en las orillas es una pésima idea.
```
knightstable = [
-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  5,  5,  0,-20,-40,
-30,  5, 10, 15, 15, 10,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 10, 15, 15, 10,  0,-30,
-40,-20,  0,  0,  0,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50]
```
##### Alfil
La idea es que eviten estar en las orillas y esquinas
```
bishopstable = [
-20,-10,-10,-10,-10,-10,-10,-20,
-10,  5,  0,  0,  0,  0,  5,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10,-10,-10,-10,-10,-20]
```
##### Torres
Deberían ocupar la septima fila y evitar las columnas a y h
```
rookstable = [
  0,  0,  0,  5,  5,  0,  0,  0,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
  5, 10, 10, 10, 10, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0]
```
##### Reina
Debería estar en el centro para así poder controlar una mayor cantidad de cuadros
```
queenstable = [
-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  5,  5,  5,  5,  5,  0,-10,
  0,  0,  5,  5,  5,  5,  0, -5,
 -5,  0,  5,  5,  5,  5,  0, -5,
-10,  0,  5,  5,  5,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20]
```
##### Rey
Al inicio el Rey se debería quedar detrás de los peones. La situación cambia conforme avanza el juego.
```
kingstable = [
 20, 30, 10,  0,  0, 10, 30, 20,
 20, 20,  0,  0,  0,  0, 20, 20,
-10,-20,-20,-20,-20,-20,-20,-10,
-20,-30,-30,-40,-40,-30,-30,-20,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30]
```

OK, esta sigo sin entender como cálcula el phase score, pero lo checamos luego

#### Situaciones Finales
Tenemos que tener una manera de poder distinguir cuando acaba un juego, por lo que utilizaremos las condiciones que ya tiene programadas la librería. Gracias a eso podemos diferenciar entre una partida ganada y un empate.
- Si hay empate o insuficiencia material, regreso `0`
- Si yo estoy haciendo el jaquemate, regreso un número demasiado grande, ejemplo `99999`
- Si yo soy el que está recibiendo el empate, regreso un número demasiado pequeño, ejemplo `-99999`

### Paso 3: Programación de las Funciones de Evaluación
Ya que tenemos las heurísticas seleccionadas, pogramamos una función de evaluación que tomé en cuenta los factores que queremos. 
##### Evaluación Material
Primero tenemos que saber cuantas piezas de cada tipo tenemos, eso se puede sacar de la siguiente manera:
```
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
```
Utilizando los valores por pieza que se dieron con anterioridad, tenemos que se puede calcular el valor material de esta forma:
```
valorMaterial = 100 * (peonB - peonN) + 320 * (caballoB - caballoN) + 330 * (alfilB - alfilN) + 500 * (torreB - torreN) + 900 * (reinaB - reinaN)
```

#### Evaluación por Posición
Utilizando las tablas que dimos anteriormente, sumamos el puntaje de cada tabla individual de acuerdo a su posición en el tablero. Nótese que se tienen que invertir verticalmente las posiciones cuando quiero calcular el valor para el otro jugador, eso lo hacemos con `chess.square_mirror(square: chess.Square)` .  De esa forma ese valor se puede sacar así
```
peonPos = sum([pawntable[i] for i in tablero.pieces(chess.PAWN, chess.WHITE)]) + sum([-pawntable[chess.square_mirror(i)] for i in tablero.pieces(chess.PAWN, chess.BLACK)])

caballoPos = sum([knightstable[i] for i in tablero.pieces(chess.KNIGHT, chess.WHITE)]) + sum([-knightstable[chess.square_mirror(i)] for i in tablero.pieces(chess.KNIGHT, chess.BLACK)])

alfilPos = sum([bishopstable[i] for i in tablero.pieces(chess.BISHOP, chess.WHITE)]) + sum([-bishopstable[chess.square_mirror(i)] for i in tablero.pieces(chess.BISHOP, chess.BLACK)])

torrePos = sum([rookstable[i] for i in tablero.pieces(chess.ROOK, chess.WHITE)]) + sum([-rookstable[chess.square_mirror(i)] for i in tablero.pieces(chess.ROOK, chess.BLACK)])

reinaPos = sum([queenstable[i] for i in tablero.pieces(chess.QUEEN, chess.WHITE)]) + sum([-queenstable[chess.square_mirror(i)] for i in tablero.pieces(chess.QUEEN, chess.BLACK)])

reyPos = sum([kingstable[i] for i in tablero.pieces(chess.KING, chess.WHITE)]) + sum([-kingstable[chess.square_mirror(i)] for i in tablero.pieces(chess.KING, chess.BLACK)])

```

#### Evaluación por Situación Final
Aquí tomamos en cuenta si en la posición actual se esta en jaquemate, insuficiencia material o empate:
```
if tablero.is_checkmate():
        if tablero.turn:
            return -9999
        else:
            return 9999
elif tablero.is_stalemate():
        return 0
else tablero.is_insufficient_material():
        return 0
```

#### Función de Evaluación
Con todo lo anterior definido, entonces la función nos queda de esta manera:
```
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

```

### Paso 4: Algoritmo de Juego
Lo que queremos es una manera de que la computadora tome las decisiones adecuadas para ganarle al jugador humano. Para esto utilizamos el algoritmo MINIMAX, lo que nos permite ver hacia adelante y hacer la mejor movida.
#### MINIMAX 
Este algoritmo funciona de acuerdo a la suposición que lo que es mejor para mí es peor para mi oponente, es un juego de suma cero. Por lo que se divide en dos, un jugador que maximiza y un jugador que quiere minimizar. Se asume siempre que mi oponente solo hace buenas jugadas. 
El pseudocódigo de está función es este:
```
function minimax(estado, profundidad, maximizar)
    if profundidad == 0 or game over in estado
        return evaluacion del estado
    
    if maximizar
        maxEval = -infinito
        for each hijo de estado
            eval = minimax(hijo, profundidad -1, false)
            maxEval = max(maxEval, eval)
        return maxEval

    else
        minEval = +infinito
        for each hijo de estado
            eval = minimax(hijo, profundidad - 1, true)
            minEval = min(minEval, eval)
        return minEval
```
Llamamos a la función de la siguiente manera:
```
minimax(estadoActual, 3, true)
```
Con esto la computadora ya podría elegir movimientos que son relativamente buenos, sin embargo no resulta práctico, por algo que se llama el [Número de Shannon](https://en.wikipedia.org/wiki/Shannon_number), el cual me da una estimación del número de jugadas posibles que puede tener una partida de ajedrez a lo largo un promedio de 40 turnos. Ese número es 10<sup>120</sup>, para tener una comparación el npumero de átomos en el universo es aproximadamente 10<sup>80</sup>. 

#### Alfa Beta Prunning
Para resolver este problema lo que vamos a hacer es encontrar una forma de no tener que calcular todos movimientos posibiles, La manera en la que hacemos esto guardando las cotas que se tienen, de tal forma que no revisemos ramas que no tienen futuro alguno. Se utilizan alfa y beta, dos parametros que me indican lo mejor que el otro jugador puede conseguir. 
- alfa es el peor puntaje para el jugador que maximiza
- beta es el peor puntaje para el jugador que minimiza
No se trata de sustituir al MINIMAX, solo de hacerlo más rápido, por lo tanto el pseudocódigo quedaría así:
```
function minimax(estado, profundidad, alfa, beta, maximizar)
    if profundidad == 0 or game over in estado
        return evaluacion del estado
    
    if maximizar
        maxEval = -infinito
        for each hijo de estado
            eval = minimax(hijo, profundidad -1, alfa, beta, false)
            maxEval = max(maxEval, eval)
            alfa = max(alfa, eval)
            if beta <= alfa
                break
        return maxEval

    else
        minEval = +infinito
        for each hijo de estado
            eval = minimax(hijo, profundidad - 1, alfa, beta,true)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha
                break
        return minEval
```
En este caso llamamos a la función de la siguiente manera:
```
minimax(estadoActual, 3, -infinito, +infinito, true)
```
#### NEGAMAX
Hay una manera de ahorrarnos lineas en la función, el procedimiento es casi el mismo, excepto que ahora vamos a trabajar mediante un supuesto `max(a,b) = -min(-a,-b)`. De esta manera solo hago un procedimiento: maximizar.
```
function negamax(estado, alfa, beta, profundidad)
    maxEval = -infinito
    if profundidad == 0 or game over en estado
        return evaluación del estado
    for each hijo de estado
        eval = -negamax(hijo, -beta, -alfa, profundidad -1)
        maxEval = max(maxEval, eval)
        alfa = max(alfa, eval)
        if alfa >= beta
            break
    return maxEval
```
Su llamada original sería:
```
negamax(estadoActual, -infinito, +infinito, 3)
```
#### Selección del movimiento
Ahora que ya tenemos una forma de obtener el mayor puntaje, necesitamos una forma de que seleccione al movimiento que nos de ese puntaje y nos regrese ese movimiento óptimo. Para eso utilizamos nuestra funcion de negamax. Con eso, el pseudocódigo quedaría así:
```
function mejorMovimiento(profundidad)
    mejorMovimiento = null
    maxEval = -999999
    alfa = -999999
    beta = 999999
    for movimiento en movimientosLegales
        hacer movimiento
        eval = -negamax(-beta, -alfa, profundidad -1)
        if eval > maxEval
            maxEval = eval
            mejorMovimiento = movimiento
        alfa = max(eval, alfa)
        saco el movimiento
    return mejorMovimiento
```
### Paso 5: Programación de la IA
Con base al pseudocódigo anterior, nos quedaron las siguientes funciones:
##### NEGAMAX
```
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
```
##### Mejor Movimiento
```
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
```
##### Función Principal
```
def main():
    tablero = chess.Board()
    while not tablero.is_game_over():
    #for i in range(16):
        #imprimeTablero(tablero)
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
            #movida = random.choice([movida for movida in tablero.legal_moves])
            movida = mejorMovimiento(tablero, 7)
            tablero.push(movida)
            #print("las negras movieron", movida)
    #imprimeTablero(tablero)
    return tablero.result()
```
#### Pruebas
Para probar el desempeño de nuestra IA, se modificó el código de tal manera que ambos jugadores fueran la computadora, sin embargo las blancas jugaban movimientos aleatorios mientras que las negras utilizaban negamax a 7 niveles de profundidad.
El código quedó de la siguiente manera:
```
def main():
    tablero = chess.Board()
    while not tablero.is_game_over():
        imprimeTablero(tablero)
        #print("")
        if tablero.turn:
            movida = random.choice([movida for movida in tablero.legal_moves])
            tablero.push(movida)
        else:
            movida = mejorMovimiento(tablero, 7)
            tablero.push(movida)
    imprimeTablero(tablero)
    return tablero.result()
```
##### Resultados
Se utilizó negamax bajando a 7 niveles de profundidad
De 100 juegos, los resultados fueron:
- `0` juegos los ganaron las blancas.
- `53` juegos los ganaron las negras.
- `47` juegos fueron empates.

### Paso 6: Mejoras
Si bien ya tenemos una IA aceptable en el juego, hay modificaciones que se pueden hacer para mejorar su rendimiento:
#### Nuevas Funciones Heurísticas
Si bien las evaluaciones que utilizamos son efectivas, son estáticas y las utilizamos para todo el juego. La principal víctima de esto es la evaluación de piezas por posición. Con ella asumimos que las posiciones de las piezas son deseables durante todo el juego, cuando las posiciones ideales cambian dependiendo de la fase del juego. 
##### Función de evaluación de PeSTO (Lo puedo pasar a mejoras)
Es una heurística desarrollada por [Ronald Friederich](https://www.chessprogramming.org/Ronald_Friederich), la cual no solo toma en cuenta el valor de las piezas y sus posiciones, sino que también que tan avanzado está el juego. Con esto se tienen diferentes tablas de posiciones para las piezas dependiendo si se está en el juego inicial, intermedio o final. 
Para esto se tiene que tener una manera de definir en que fase se está, por lo que se utiliza una especie de "puntaje de fase"

#### Movidas iniciales
Por el momento, las jugadas iniciales que hace la computadora siempre son las mismas, exactamente `g8f6` y`b8c6`, por lo que no es un jugador muy creativo que digamos. Lo que podríamos hacer es darle un libro de movidas iniciales (la librería me lo permite) para que tenga más opciones y comience las partidas de diferente manera.

#### Resolver el [Efecto Horizonte](https://www.chessprogramming.org/Horizon_Effect)
Esto se sucede debido a la limitación de la profundidad en los árboles de búsqueda.La principal manifestación de esto es cuando un resultado negativo parace que es evitable cuando en realidad solamente se puede posponer. Un ejemplo de esto es cuando en el movimiento 6 vemos que la Reina es capturada, de tal forma que se sacrificarán piezas para evitar eso. Lo que no nos damos cuenta es que en el movimiento 10 la Reina de todas formas será capturada, por lo que se hizó un sacrificio inútil. 

Para resolver este problema, se utiliza la [Quiescence Search](https://www.chessprogramming.org/Quiescence_Search), la cual se realiza una búsqueda limitada al final del programa. Su objetivo es evaluar posiciones "quietas" es decir aquellas donde no se pueden capturar piezas. 
El pseudocódigo de la función es: 
```
int Quiesce( int alpha, int beta ) {
    int stand_pat = Evaluate();
    if( stand_pat >= beta )
        return beta;
    if( alpha < stand_pat )
        alpha = stand_pat;

    until( every_capture_has_been_examined )  {
        MakeCapture();
        score = -Quiesce( -beta, -alpha );
        TakeBackMove();

        if( score >= beta )
            return beta;
        if( score > alpha )
           alpha = score;
    }
    return alpha;
}
```
Necesitamos encontrar una manera de dejar de buscar sin necesariamente realizar todas las busquedas posibles. El stand_pat se trata de tener una cota inferior para el puntaje. Si stand_pat es mayor o igual a beta entonces podemos regresar beta como puntaje, de otra manera la búsqueda continúa. 
Nuestro código quedaría de la siguiente manera:
```
def quiesce(tablero, alfa, beta):
    stand_pat = evaluar(tablero)
    if (stand_pat >= beta):
        return beta

    alfa=max(alfa, stand_pat)

    for movida in tablero.legal_moves:
        if tablero.is_capture(movida):
            tablero.push(movida)
            puntaje = -quiesce(tablero,-beta, -alfa)
            tablero.pop()

            if (puntaje >= beta):
                return beta

            alfa=max(alfa, puntaje)
    return alfa
```
De igual manera tenemos que modificar nuestra función de negamax:
```
def negamax(tablero, alfa, beta, profundidad):
    maxEval = -999999
    if profundidad == 0 or not tablero.is_game_over():
        return quiesce(tablero, alfa, beta)
    for movida in tablero.legal_moves:
        tablero.push(movida)
        valorEval = -(negamax(tablero, -beta, -alfa, profundidad-1))
        tablero.pop()
        maxEval = max(maxEval, valorEval)
        alfa = max(alfa, valorEval)
        if alfa >= beta:
            break
    return maxEval
```
Corrimos en problemas con este método, la computadora ahora se tardaba más tiempo por jugada, lo máximo que se conto fueron 10 segundos entre que el humano daba una movida y la computadora respondía. Sin embargo necesitabamos comparar su desempeño con la versión anterior. Tuvimos que reducir el nivel de profundidad de 7 a 3, de otra forma se tarda demasiado tiempo. 
Se volvieron a realizar pruebas, con las blancas jugando de manera aleatoria y las negras jugando con el nuevo algoritmo de negamax, los resultados fueron los siguientes:
- `0` juegos los ganaron las blancas
- `88` juegos los ganaron las negras
- `12` juegos fueron empatados
### Paso 7: Una Nueva IA Mejorada
