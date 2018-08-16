import React, { Component } from 'react';

class NavHeader extends Component {
    render() {
        return (
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <span class="navbar-brand mb-0 h1">TwitchViewer</span>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                    <div class="navbar-nav">
                        <a class="nav-item nav-link" href="/">Popular</a>
                        <a class="nav-item nav-link" href="/">Games</a>
                        <a class="nav-item nav-link" href="/">Settings</a>
                    </div>
                </div>
            </nav>
            

        );
    }
} 

export default NavHeader;