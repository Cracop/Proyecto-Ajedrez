import axios from 'axios';
const URL = 'http://localhost:8000';

export default class CustomersService{

    constructor(){}


    getCustomers() {
        const url = `${URL}/`;
        return axios.get(url).then(response => response.data);
    }

}