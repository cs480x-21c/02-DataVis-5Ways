/**
 * StartGame.js
 * date created: 2/12/2021
 * Author: Benjamin M'Sadoques
 *
 * Provies functions to control the plot
 *
 * Some code taken from:
 * https://www.d3-graph-gallery.com/scatter
 *
 * Also uses D3 annotation:
 * https://d3-annotation.susielu.com/
 */

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
    svg.append("g")
        .attr("id", "scatterPlot")
        .selectAll("dot")
        .data(data)
        .enter()
        .append("circle")
        .attr("id", function (d) { return "c" + Object.values(d)[0] })
        .attr("class", function (d) { return d.Manufacturer })
        .attr("cx", function(d) { return xScale(d.Weight)})
        .attr("cy", function(d) { return yScale(d.MPG)})
        .attr("r", function(d) { return rScale(d.Weight) })
        .style("fill", function(d) { return cScale(d.Manufacturer)})
        .on("mouseover", function (e, d)
        {
            changeCircleOpacity(d, 1.0);
            addAnnotation(d, this);
        })
        .on("mouseleave", function(e, d)
        {
            changeCircleOpacity(d, 0.5);
            removeId("#vis","#annotation");
        });
}

/**
 * Changes the opacity of any circles that match the manufacturer
 * @param data data point
 * @param opacity what to set the circle opacity to
 */
function changeCircleOpacity(data, opacity)
{
    d3.selectAll("." + data.Manufacturer)
        .transition()
        .style("fill", d3.color(cScale(data.Manufacturer)).copy({opacity:opacity}));
}

/**
 * Adds an annotation to the current data point
 * @param data data point
 * @param selected current circle to attach the annotation
 */
function addAnnotation(data, selected)
{
    // Custom annotation for cars
    let annotations = [
        {
            note: {
                // could not find how to do a line break
                title: data.Car,
                label: "MPG: " + data.MPG + " " +
                    "Weight: " + data.Weight,
                align: "left",
                wrap: 200,
            },
            x: selected.cx.baseVal.value,
            y: selected.cy.baseVal.value,
            dy: 0,
            dx: 15,
        }
    ]

    // Adds the annotation, the ID is used for removing it
    d3.select('#vis')
        .append("g")
        .attr("id", "annotation")
        .call(d3.annotation()
            .annotations(annotations));
}

/**
 * removes the current ID from the vis
 * @param vis to remove the id from
 * @param id to remove
 */
function removeId(vis, id)
{
    d3.select(vis).select(id).remove();
}
