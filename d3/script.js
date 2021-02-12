// d3.csv("cars-sample.csv").then(function(data) {
//     for (var i = 0; i < data.length; i++){
//         console.log(data[i])
//     }
// });

let values = []
window.onload = function(){
    for (var i = 0; i < 200; i++){
        values.push(1)
    }
    console.log(values)
}

let xScale, yScale

let width = 800
let height = 600
let padding = 40

let svg = d3.select('#scatter').attr('width', width).attr('height', height)
let div = d3.select('body')
    .append('div')
    .attr('id', 'tooltip')
    .attr('style', 'position: absolute; opacity: 0;');


function drawScale(){
    xScale = d3.scaleLinear().domain([1400,5000]).range([padding, width-padding])
    yScale = d3.scaleLinear().domain([7,40]).range([height-padding, padding])
}

function drawAxis(){
    let xAxis = d3.axisBottom(xScale).ticks(6)
    let yAxis = d3.axisLeft(yScale).ticks(6)
    svg.append('g').call(xAxis).attr('id', 'x-axis')
        .attr('transform', 'translate(0,'+(height-padding)+')')
    svg.append('g').call(yAxis).attr('id', 'y-axis')
        .attr('transform', 'translate('+padding+',0)')
}

function drawScatter(){
    d3.csv("cars-sample.csv").then(function(data) {
        svg.selectAll('circle')
            .data(values)
            .enter()
            .append('circle')
            .attr('cx', function(d, i){
                if (i < data.length && i !== 0) {
                    return xScale(data[i]['Weight'])
                }
            })
            .attr('cy', function(d, i){
                if (i < data.length && i !== 0 && data[i]['MPG']!=='NA') {
                    return yScale(data[i]['MPG'])
                }
            })
            .attr('r', function(d, i){
                if (i < data.length && i !== 0 && data[i]['MPG']!=='NA') {
                    return data[i]['Weight']/300
                }
            })
            .attr('fill', function(d, i){
                if (i < data.length && i !== 0 && data[i]['Manufacturer']==='bmw'){
                    return 'pink'
                }
                else if (i < data.length && i !== 0 && data[i]['Manufacturer']==='ford'){
                    return 'green'
                }
                else if (i < data.length && i !== 0 && data[i]['Manufacturer']==='honda'){
                    return 'cyan'
                }
                else if (i < data.length && i !== 0 && data[i]['Manufacturer']==='mercedes'){
                    return 'orange'
                }
                else return 'purple'
            })
            .attr('style', 'opacity:0.5')
            .on('mouseover', function(d, i) {
                if (i < data.length && i !== 0) {
                    d3.select('#tooltip').style('opacity', 1).text(data[i]['Car']+", "+
                        data[i]['Origin'])
                        .style("left", d3.select(this).attr('cx') + "px")
                        .style("top", (d3.select(this).attr('cy') - 30) + "px")
                }
            })
            .on('mouseout', function() {
                d3.select('#tooltip').style('opacity', 0)
            })
    });


}

drawScale()
drawScatter()
drawAxis()
