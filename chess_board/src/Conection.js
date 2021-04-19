import axios from 'axios';
const URL = 'http://localhost:8000/chess';

export default class Connection{

    constructor(){

    }


    getStart() {
        const url = `${URL}/`;
        return axios.get(url).then(response => response.data);
    }

    movimiento( move ) {
        const url = `${URL}/${move}`
        return axios.get(url).then(response => response.data)
    }

}