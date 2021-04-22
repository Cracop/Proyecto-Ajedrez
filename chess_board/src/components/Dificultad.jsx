import { Component } from "react"

class Dificultad extends Component{
    mode = () => {
        if(this.props.mode ===0){
            return "Fácil"
        } else if(this.props.mode === 1){
            return "Medio"
        } else {
            return "Difícil"
        }
    }  

    render(){
        return(
            <div >
                <div className="row">
                    <div className="col s12">
                        <h4 className="white-text center">Dificultad actual: {this.mode()}</h4>
                    </div>
                    <div className="input-field col s12 center">
                        <input 
                            type="button" 
                            value="Fácil" 
                            className="waves-effect waves-ligh btn blue accent-3"
                            onClick={this.props.onClick}
                        />
                    </div>
                    <div className="input-field col s12 center">
                        <input 
                            type="button" 
                            value="Medio" 
                            className="waves-effect waves-ligh btn blue accent-3"
                            onClick={this.props.onClick}
                        />
                    </div>
                    <div className="input-field col s12 center">
                        <input 
                            type="button" 
                            value="Difícil"
                            onClick={this.props.onClick} 
                            className="waves-effect waves-ligh btn blue accent-3"
                        />
                    </div>
                    <div className="input-field col s12 center">
                        <input 
                            type="button" 
                            value="PC vs PC" 
                            className="waves-effect waves-ligh btn red accent-3"
                            onClick={this.props.onClick}
                        />
                    </div>
                </div>
            </div>
        )
    }
}

export default Dificultad