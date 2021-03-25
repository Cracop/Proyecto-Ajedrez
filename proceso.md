#Proceso de la creación de una IA capaz de jugar ajedrez contra un humano
##Guía sobre como funciona la librería de Chess
Se hizo con el objetivo de poder implenetarla de manera correcta

### Liberías importadas
    -chess
    -random

###Creación del tablero
Se utiliza 'tablero = chess.Board()' para crear un tablero, el parametro que se le pasa es la notación FEN del estado del tablero que queremos.
    -Si no se le pasa nada, por default te crea el tablero en su estado inicial
    -Si se le pasa 'None' se crea un tablero vació

###Implementación del tablero
