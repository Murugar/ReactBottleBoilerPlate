import React, { Component } from 'react';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        This is a test 
        Using { this.props.api }
      </div>
    );
  }
}

export default App;
