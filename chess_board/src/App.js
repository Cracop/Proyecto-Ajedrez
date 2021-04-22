import ChessBoard from './components/ChessBoard'
import { BrowserRouter as Router, Route, Link } from "react-router-dom";


import 'materialize-css/dist/css/materialize.min.css'
import './styles/App.css'

function App() {
	
	return (
	
		<Router>
			<Route path="/" exact component={ChessBoard}/>	
		</Router>
				

	);

}

export default App;
