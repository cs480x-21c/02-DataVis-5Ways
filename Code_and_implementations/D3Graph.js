import React, { Component } from 'react';
import * as d3 from 'd3';
import Button from "@material-ui/core/Button";

class D3Graph extends Component {

  constructor(props) {
    super(props);
    this.myRef = React.createRef();
    this.state = { windowWidth: window.innerWidth,
                   windowHeight: window.innerHeight };
  }

  handleResize = (e) => {
    this.setState({ windowWidth: window.innerWidth,
                    windowHeight: window.innerHeight});
  };

  componentDidMount() {
    //Responsive Sizing
    window.addEventListener("resize", this.handleResize);
    let { windowWidth, windowHeight } = this.state; 
    let w = windowWidth / 2;
    let h = windowHeight / 2; 

    var margin = {top: 10, right: 30, bottom: 30, left: 60};

    //Create Background Region
    var svg = d3.select(this.myRef.current)
    .append("svg")
    .attr("width", w + margin.left + margin.right)
    .attr("height", h + margin.top + margin.bottom)
    .style("background-color", "white")
    .append("g") //Add graph tag
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

    var colors = ["#00008B",
                  "#003EFF",
                  "#00611C",
                  "#00AF33",
                  "#00CD00",
                  "#00CED1",
                  "#659D32",
                  "#660198",
                  "#68228B",
                  "#687E5A",
                  "#68838B",
                  "#691F01",
                  "#964514"];

    var manufacturers = [];
    //Load data and the magic happens
    d3.csv("/cars-sample.csv").then(function(data) {
        data.forEach(function(d) {
          d.MPG = +d.MPG;
          d.Cylinders = +d.Cylinders;
          d.Displacement = +d.Displacement;
          d.Horsepower = +d.Horsepower;
          d.Weight = +d.Weight;
          d.Acceleration = +d.Acceleration;
          d["Model.Year"] = +d["Model.Year"];
          
        if(manufacturers.indexOf(d.Manufacturer) === -1){
            manufacturers.push(d.Manufacturer);
        }
          
        });
        var x = d3.scaleLinear()
            .domain([0, 5000])
            .range([ 0, w ]);
        
        svg.append("g")
            .attr("transform", "translate(0," + h + ")")
            .call(d3.axisBottom(x).ticks(4));
        
        // Add Y axis
        var y = d3.scaleLinear()
            .domain([0, 40])
            .range([ h, 0]);

             // text label for the x axis
        svg.append("text")             
            .attr("transform",
                    "translate(" + (w/2) + " ," + 
                                (h + margin.top + 20) + ")")
            .style("text-anchor", "middle")
            .text("MPG");


        // text label for the y axis
        svg.append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 0 - margin.left)
            .attr("x",0 - (h / 2))
            .attr("dy", "1em")
            .style("text-anchor", "middle")
            .text("Weight");      

        svg.append("g")
        .call(d3.axisLeft(y));

        svg.append('g')
            .selectAll("dot")
            .data(data)
            .enter()
            .append("circle")
            .attr("cx", function (d) { return x(d.Weight); } )
            .attr("cy", function (d) { return y(d.MPG); } )
            .attr("r",  function (d) { return 0.003 * d.Weight; } )
            .style("opacity", 0.5)
            .style("fill", function (d) { return colors[manufacturers.indexOf(d.Manufacturer)]; })

      });

  }

  componentWillUnmount() {
    window.addEventListener("resize", this.handleResize);
  } 

  render() {
    return <div className="d3Graph">
              <div ref={this.myRef}>
              </div>  
           </div>
  }
} 

export default D3Graph;