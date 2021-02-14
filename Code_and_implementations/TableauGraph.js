import React, { Component } from 'react';
import { Link } from "react-router-dom";
import Button from "@material-ui/core/Button";

class TableauGraph extends Component {

    state = {
    };

    render() {
        return (
            <div className="cs4802P2Div">
                <div className="imagecontainer">
                    <img img src="/TableauGraph.PNG" alt="Tableau Graph"/>
                    <h5>Made with Tableau</h5>
                </div>
            </div>
        );
    }
}
 
export default TableauGraph;