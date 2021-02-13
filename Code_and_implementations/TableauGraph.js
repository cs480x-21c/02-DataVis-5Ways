import React, { Component } from 'react';
import { Link } from "react-router-dom";
import Button from "@material-ui/core/Button";

class TableauGraph extends Component {

    state = {
    };

    render() {
        return (
            <div className="navigationMenu">
                <div className="imagecontainer">
                    <img img src="/TableauGraph.PNG" alt="Tableau Graph"/>
                </div>
            </div>
        );
    }
}
 
export default TableauGraph;