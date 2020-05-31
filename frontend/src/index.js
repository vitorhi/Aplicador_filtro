import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import axios from 'axios';


class App extends React.Component {
	state = {url:' ', filter:'Gaussian Blur', intensity:' ' , photos:' '};
	constructor(props) {
	  	super(props);
	  	this.handleUrlChange = this.handleUrlChange.bind(this);
	  	this.handleClick = this.handleClick.bind(this);	  	
	  	this.handleFilterChange = this.handleFilterChange.bind(this);	  	
	  	this.handleIntensityChange = this.handleIntensityChange.bind(this);	  	
  	}
  	hexToBase64(str) {
    	return btoa(String.fromCharCode.apply(null, str.replace(/\r|\n/g, "").replace(/([\da-fA-F]{2}) ?/g, "0x$1 ").replace(/ +$/, "").split(" ")));
	}
	async handleClick(e) {
		e.preventDefault();
		console.log(this.state);
		
    	const response = await axios.post("http://127.0.0.1:5000/",(this.state));
    	


	}

	handleUrlChange(e) {
   		this.setState({[e.target.name]: e.target.value});
	}
	handleFilterChange(e) {
   		this.setState({[e.target.name]: e.target.value});
	}
	handleIntensityChange(e) {
   		this.setState({[e.target.name]: e.target.value});
	}
  render() {
    return (

      <body>
      <h1>Filtro de imagens</h1>
      <form>
		<label for="fname">Url da imagem:</label>
		<input 
			type="text" 
			name="url"
			value={this.state.value} 
			onChange={(e) => this.handleUrlChange(e)}
		/> <br></br>

		<label for="filters">Selecione o filtro desejado:</label>
		<select name="filter" id="filter" value={this.state.value} onChange={(e) => this.handleFilterChange(e)}>
			<optgroup label="Blur">
			  <option value="Gaussian Blur">Gaussian Blur</option>
			  <option value="Median Blur">Median Blur</option>
			</optgroup>
			<optgroup label="Enhance">
			  <option value="Denoiser Enhance">Denoiser Enhance</option>
			  <option value="Unsharp Enhance">Unsharp Enhance</option>
			</optgroup>
			<optgroup label="Edge">
			  <option value="Laplacian Edge">Laplacian Edge</option>
			</optgroup>
			<optgroup label="Others">
			  <option value="Erode">Erode</option>
			  <option value="Dilate">Dilate</option>
			</optgroup>
		</select><br></br>
		<label for="fname">Valor da intensidade do filtro:</label>
		<input 
			className="numBox" 
			min="2" 
			type="number" 
			id="intensity" 
			name="intensity"	
			value={this.state.value} 
			onChange={(e) => this.handleFilterChange(e)}>
		</input><br></br>
	  	
	  	<button onClick={this.handleClick}>
				Enviar
		</button>
	  </form>
	  
      </body>
    );
  }
}

// ========================================

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
