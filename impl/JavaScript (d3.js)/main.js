// Static dimensions and margins of the graph
// From https://www.d3-graph-gallery.com/graph/custom_theme.html
let margin = {top: 10, right: 30, bottom: 40, left: 50},
    width = 500 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

function main() {
    // Test if d3 is loaded
    console.log(d3);

    // Setup svg
    let svg = d3.select("#target")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    // Create tooltip div
    let div = d3.select("body").append("div")
        .attr("id", "tooltip")
        .attr("class", "card")
        .style("opacity", 0);

    // Load CSV data
    d3.csv("cars-sample.csv")
        .then(data => {
            console.log(data);

            // Create X axis
            let x = d3.scaleLinear()
                .domain([1500, 5100])
                .range([0, width]);

            // Add X axis to SVG
            svg.append("g")
                .attr("transform", "translate(0," + height + ")")
                .call(d3.axisBottom(x).ticks(4));

            // Add X axis label to SVG
            svg.append("text")
                .attr("text-anchor", "end")
                .attr("x", width/2 + margin.left)
                .attr("y", height + margin.top + 20)
                .text("Weight");

            // Create Y axis
            let y = d3.scaleLinear()
                .domain([8, 47])
                .range([height, 0]);

            // Add Y axis to SVG
            svg.append("g")
                .call(d3.axisLeft(y).ticks(4));

            // Add Y axis label to SVG
            svg.append("text")
                .attr("text-anchor", "end")
                .attr("transform", "rotate(-90)")
                .attr("y", -margin.left + 20)
                .attr("x", -margin.top - height/2 + 20)
                .text("MPG");

            // Filter out N/A MPG data
            data = data.filter(d => d.MPG !== "NA");

            // Add dots to graph
            svg.append('g')
                .selectAll("dot")
                .data(data)
                .enter()
                .append("circle")
                .attr("cx", function (d) { return x(d.Weight); } )
                .attr("cy", function (d) { return y(d.MPG); } )
                .attr("r", function(d) {
                    return (d.Weight / 1000) * 2;
                })
                .style("fill", function (d) {
                    switch (d.Manufacturer) {
                        case "bmw":
                            return "#FF0000";
                        case "ford":
                            return "#83814d";
                        case "honda":
                            return "#00FF00";
                        case "mercedes":
                            return "#0099ff";
                        case "toyota":
                            return "#FF00FF";
                        default:
                            return "#000000";
                    }
                })
                .on("mouseover", function(e, d) {
                    div.transition()
                        .duration(200)
                        .style("opacity", 1);
                    div	.html("Car: " + d.Manufacturer + " " + d.Car + "<br/>"
                    + "MPG: " + d.MPG + "<br/>"
                    + "Cylinders: " + d.Cylinders + "<br/>"
                    + "Displacement: " + d.Displacement + "<br/>"
                    + "Horsepower: " + d.Horsepower + "<br/>"
                    + "Weight: " + d.Weight + "<br/>"
                    + "Acceleration: " + d.Acceleration + "<br/>"
                    + "Model Year: " + d["Model.Year"] + "<br/>"
                    + "Origin: " + d.Origin + "<br/>")
                        .style("left", (e.pageX) + "px")
                        .style("top", (e.pageY - 28) + "px");
                })
                .on("mouseout", function() {
                    div.transition()
                        .duration(200)
                        .style("opacity", 0);
                })
                .style("opacity", 0.5);
        });
}