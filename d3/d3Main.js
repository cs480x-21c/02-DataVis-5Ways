/**
 * StartGame.js
 * date created: 2/10/2021
 * Author: Benjamin M'Sadoques
 *
 * Provides all the hard-coded values to make the vis
 * Provides the main method to draw the plot
 * Some code taken from:
 * https://www.d3-graph-gallery.com/scatter
 */

// pixel size taken from the image provided (exact)
const width = 616;
const height = 439;

const margin = {top: 8, bottom: 41, left: 53, right: 111};
const plot = {width: 452, height: 390};

const xLabel = {x:"235", y:"430", text:"Weight"};
const yLabel = {x:"30", y:"217", text:"MPG"};

// xScale starts at about 1500 and ends at about 5100
const xScale = d3.scaleLinear()
    .domain([1500, 5100])
    .range([margin.left, plot.width]);

// yScale starts at about 8 and ends at about 45
const yScale = d3.scaleLinear()
    .domain([8, 45])
    .range([margin.top + plot.height, margin.top]);

// axis, uses for defining tick values
const xAxis = d3.axisBottom(xScale).tickValues([2000, 3000, 4000, 5000]);
const yAxis = d3.axisLeft(yScale).tickValues([10, 20, 30, 40]);

// measurements estimated from the picture
const rScale = d3.scaleLinear()
    .domain([1500, 5100])
    .range([3, 10]);

// Colors taken from the picture, Opacity was specified to be half
const cScale = d3.scaleOrdinal()
    .domain(["bmw", "ford", "honda", "mercedes", "toyota"])
    .range(["#F779737F","#B0B24B7F", "#31BC807F",
        "#2FB1F67F", "#E86DF17F"]);

/**
 * the main method that makes the plot
 * @param data
 */
function d3Main(data)
{
    let svg = d3.select('#vis')
        .attr("width", width)
        .attr("height", height);

    // Add the x and y axes
    addAxis(svg, 0, (margin.top + plot.height), xAxis);
    addAxis(svg, margin.left, 0, yAxis);

    // Add the axes labels
    addAxisLabel(svg, xLabel.x, xLabel.y, xLabel.text);
    // y axis label needs to be rotated
    addAxisLabel(svg, yLabel.x, yLabel.y, yLabel.text)
        .attr("transform", "rotate(270, " + yLabel.x + ", " + yLabel.y + ")");

    drawPlot(svg, data);
}

/**
 * adds an axis
 * @param svg
 * @param x position
 * @param y position
 * @param axis
 * @returns {*} the new axis
 */
function addAxis(svg, x, y, axis)
{
    return svg.append("g")
        .attr("transform", "translate(" + x + ", " + y + ")")
        .call(axis);
}

/**
 * Adds the axis labels
 * @param svg
 * @param x position
 * @param y position
 * @param text for the axis
 * @returns {*} the new axis label
 */
function addAxisLabel(svg, x, y, text)
{
    return svg.append("text")
        .attr("x", x)
        .attr("y", y)
        .text(text);
}

/**
 * Draws the plot data to the svg
 * @param svg
 * @param data
 */
function drawPlot(svg, data)
{
    svg.append('g')
        .attr("id", "scatterPlot")
        .selectAll("dot")
        .data(data)
        .enter()
        .append("circle")
            .attr("class", function (d) { return d.Manufacturer })
            .attr("cx", function(d) { return xScale(d.Weight)})
            .attr("cy", function(d) { return yScale(d.MPG)})
            .attr("r", function(d) { return rScale(d.Weight) })
            .style("fill", function(d) { return cScale(d.Manufacturer)})
            .on("mouseover", function (e, d) { changeCircleOpacity(d, 1.0); })
            .on("mouseleave", function(e, d) { changeCircleOpacity(d, 0.5); });
}

function changeCircleOpacity(d, opacity)
{
    d3.selectAll("." + d.Manufacturer)
        .transition()
        .style("fill", d3.color(cScale(d.Manufacturer)).copy({opacity:opacity}));
}