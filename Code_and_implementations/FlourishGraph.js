import React, { Component } from 'react';
import { Link } from "react-router-dom";
import Button from "@material-ui/core/Button";

class FlourishGraph extends Component {

    state = {
    };

    render() {
        return (
            <div className="navigationMenu">
                <div className="imagecontainer">
                    <img img src="/FlourishGraph.png" alt="Tableau Graph"/>
                </div>
            </div>
        );
    }
}
 
export default FlourishGraph;