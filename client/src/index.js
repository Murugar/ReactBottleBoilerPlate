import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';

/* use this API when running in dev mode */
const api = "http://localhost:8080/api/";
/* use this API when building the application for deployment */
// const API = "/api/";

ReactDOM.render(<App api={ api }/>, document.getElementById('root'));
registerServiceWorker();
