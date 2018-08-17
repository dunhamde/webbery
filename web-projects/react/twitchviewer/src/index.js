import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
//import 'bootstrap';
import './index.css';
//import 'bootstrap/dist/css/bootstrap.min.css';

import NavHeader from './components/nav_header';
import MainStream from './components/main_stream';

// import reducers from './reducers';

ReactDOM.render(
    <BrowserRouter>
    <div>
        <NavHeader />
        {/* <MainStream /> */}
        <p>This is a test of the new color I am trying to add to this application for twitch.tv streams</p>
    </div>
    </BrowserRouter>
, document.querySelector('.container'));