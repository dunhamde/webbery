import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

import NavHeader from './components/nav_header';
import MainStream from './components/main_stream';

// import reducers from './reducers';

ReactDOM.render(
    <div>
        <NavHeader />
        <MainStream />
    </div>
, document.querySelector('.container'));