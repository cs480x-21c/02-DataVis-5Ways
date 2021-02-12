margin = {top: 10, right: 30, bottom: 30, left: 60},
    width = 460 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

var svg = d3.select("#dataviz")
    .append("svg")
      .attr("width", 5000)
      .attr("height", 5000)
    .append("g")
      .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

d3.csv("cars-sample.csv").then(function(data){

    var colors = {"bmw":"lightcoral","ford":"olive","honda":"green","mercedes":"cornflowerblue","toyota":"fuchsia"}

    console.log(data)
    // Add X axis
    var x = d3.scaleLinear()
        .domain([1500, 5000])
        .range([ 0, width ]);
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));
    
    // Add Y axis
    var y = d3.scaleLinear()
        .domain([8, 48])
        .range([ height, 0]);
    svg.append("g")
        .call(d3.axisLeft(y));
    
    // Add dots
    svg.append('g')
        .selectAll("dot")
        .data(data)
        .enter()
        .append("circle")
        .attr("cx", function (d) { return x(d.Weight); } )
        .attr("cy", function (d) { return y(d.MPG); } )
        .attr("r", function (d) { return d.Weight/700; } )
        .attr("opacity", "0.5" )
        .style("fill", function (d) { return colors[d.Manufacturer]; })
    
    })

    svg.append("text")
    .attr("x", 200)
    .attr("y", 400)
    .style("text-anchor", "middle")
        .text("Weight");

    svg.append("text")
    .attr("transform", "rotate(-90)")
    .attr("x", -180)
    .attr("y", -30)
    .style("text-anchor", "middle")
        .text("MPG");