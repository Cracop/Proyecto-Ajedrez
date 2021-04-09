import { Component, useRef } from "react"
import Tile from "./Tile"
import Chess from "./Chess"

import './styles/ChessBoard.css'

const verticalAxis = [1, 2, 3, 4, 5, 6, 7, 8]
const horizontalAxis = ["a", "b", "c", "d", "e", "f", "g", "h"]

const TeamType = {
    BLACK: 'BLACK',
    WHITE: 'WHITE'
}

const PieceType = {
    PAWN: 'PAWN',
    BISHOP: "BISHOP",
    KNIGHT: 'KNIGHT',
    ROOK: 'ROOK',
    QUEEN: 'QUEEN',
    KING: 'KING'
}

const initialBoardState = []
for(let p = 0; p < 2; p++){
    const type = p === 0 ? "black" : "white"
    const y = p === 0 ? 7 : 0
    initialBoardState.push(
        // Torres
        {
            image: `assets/images/chess-rook-${type}.png`,
            x: 0,
            y,
            type: PieceType.ROOK,
        },
        {
            image: `assets/images/chess-rook-${type}.png`,
            x: 7,
            y,
            type: PieceType.ROOK,
        },
        // Caballos
        {
            image: `assets/images/chess-knight-${type}.png`,
            x: 1,
            y,
            type: PieceType.KNIGHT,
        },
        {
            image: `assets/images/chess-knight-${type}.png`,
            x: 6,
            y,
            type: PieceType.KNIGHT,
        },
        // Alfiles
        {
            image: `assets/images/chess-bishop-${type}.png`,
            x: 2,
            y,
            type: PieceType.BISHOP,
        },
        {
            image: `assets/images/chess-bishop-${type}.png`,
            x: 5,
            y,
            type: PieceType.BISHOP,
        },
        //Reyes
        {
            image: `assets/images/chess-king-${type}.png`,
            x: 4,
            y,
            type: PieceType.KING,
        },
        //Reinas
        {
            image: `assets/images/chess-queen-${type}.png`,
            x: 3,
            y,
            type: PieceType.QUEEN,
        },
    )
}
for(let i = 0; i < 8; i++){
    initialBoardState.push({
        image: "assets/images/chess-pawn-black.png",
        x: i,
        y: 6,
        type: PieceType.PAWN,
    })
    initialBoardState.push({
        image: "assets/images/chess-pawn-white.png",
        x: i,
        y: 1,
        type: PieceType.PAWN,
    })
}

class ChessBoard extends Component{

    board = []
    state = {
        pieces: initialBoardState,
        girdX: 0,
        gridY: 0,
        offsetLeft: 0,
        offsetTop: 0,
        clientWidth: 0,
        clientHeight: 0,
        activePiece: null,
    }
    constructor(){
        super()
        for(let j = verticalAxis.length - 1; j >= 0; j--){
            for(let i = 0; i < horizontalAxis.length; i++){

                const number = i + j + 2;
                let image = undefined;
                
                this.state.pieces.forEach(p => {
                    if(p.x === i && p.y === j){
                        image = p.image
                    }
                });

                this.board.push(
                    <Tile
                        number={number}
                        image={image}
                        key={`${j},${i}`}
                    />
                )

            }
        }
        //this.ponerTablero()
       
    }
    // Llena cada casilla del tablero
    ponerTablero = () => {
        this.board = []
        for(let j = verticalAxis.length - 1; j >= 0; j--){
            for(let i = 0; i < horizontalAxis.length; i++){

                const number = i + j + 2;
                let image = undefined;
                
                this.state.pieces.forEach(p => {
                    if(p.x === i && p.y === j){
                        image = p.image
                    }
                });

                this.board.push(
                    <Tile
                        number={number}
                        image={image}
                        key={`${j},${i}`}
                    />
                )

            }
        }
    }

    componentDidMount = (e) => {
        this.setState({
            ...this.state,
            offsetLeft: document.getElementById('chessboard').offsetLeft,
            offsetTop: document.getElementById('chessboard').offsetTop,
            clientWidth: document.getElementById('chessboard').clientWidth,
            clientHeight: document.getElementById('chessboard').clientHeight,
        })
    }

    activePiece = null
    grabPiece = (e) => {
        const element = e.target
        //console.log(element);
        if(element.classList.contains("chess-piece")){
            const gridX = Math.floor((e.clientX - this.state.offsetLeft) / 60)
            const gridY = Math.abs(Math.ceil((e.clientY - this.state.offsetTop - 480) / 60))
            console.log(gridX, gridY);
            this.setState({
                ...this.state,
                gridX: gridX,
                gridY: gridY,
            })
            const x = e.clientX - 30
            const y = e.clientY -30
            element.style.position = "absolute"
            element.style.left = `${x}px`
            element.style.top = `${y}px`
            this.activePiece = element
        }
    }

    movePiece = (e) => {
        if(this.activePiece){
            const minX = this.state.offsetLeft - 15
            const minY = this.state.offsetTop - 15
            const maxX = this.state.offsetLeft + this.state.clientWidth - 45
            const maxY = this.state.offsetTop + this.state.clientHeight - 45
            const x = e.clientX - 30
            const y = e.clientY - 30
            this.activePiece.style.position = "absolute" 
           

            if(x < minX){
                this.activePiece.style.left = `${minX}px`
            } else if(x > maxX){
                this.activePiece.style.left = `${maxX}px`
            } else {
                this.activePiece.style.left = `${x}px`
            }

            if(y < minY){
                this.activePiece.style.top = `${minY}px`
            } else if(y > maxY){
                this.activePiece.style.top = `${maxY}px`
            } else {
                this.activePiece.style.top = `${y}px`
            }
            
        }    
    }

    dropPiece = (e) => {
        if(this.activePiece){
            const x = Math.floor((e.clientX - this.state.offsetLeft) / 60)
            const y = Math.abs(Math.ceil((e.clientY - this.state.offsetTop - 480) / 60))                        
            
            this.state.pieces.map((p) =>{
                    if(p.x === this.state.gridX && p.y === this.state.gridY){
                        
                        p.x = x
                        p.y = y
                    
                    }
                    return p
            })
            console.log(x, y);
            
            this.activePiece = null
        }
        this.ponerTablero()
        this.forceUpdate()
    }

 
    render(){
        
        return(

            <div 
                id="chessboard"
                onMouseMove={e => this.movePiece(e)} 
                onMouseDown={ e => this.grabPiece(e) }
                onMouseUp={e => this.dropPiece(e)}
            >
                <Chess board={this.board} />
            </div>

        )

    }

}

export default ChessBoard;