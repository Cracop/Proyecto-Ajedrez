import React from 'react'

import './styles/ChessBoard.css'

const Chess = (props) => {
    return(
        <div id="chessboard">
            {props.board}
        </div>
    )    
}

export default Chess