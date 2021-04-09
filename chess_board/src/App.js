import ChessBoard from './components/ChessBoard'

import 'materialize-css/dist/css/materialize.min.css'
import './styles/App.css'

function App() {
	
	return (
		<div className="container">

			<div className="row">	
				<div className="col s12" id="app">
				
					<ChessBoard />
				
				</div>	
			</div>
		</div>

	);

}

export default App;
