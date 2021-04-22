import axios from 'axios';
//const URL = 'http://localhost:8000/chess';
const URL = 'http://iachessgame.herokuapp.com/chess';

export default class Connection{

    constructor(){}


    getStart() {
        const url = `${URL}/`;
        return axios.get(url).then(response => response.data);
    }

    movimiento( move, mode ) {
        const url = `${URL}/${move}/${mode}`
        return axios.get(url).then(response => response.data)
    }

    automatic_move( level ) {
        const url = `${URL}/${level}`
        return axios.get(url).then(response => response.data)
    }

}