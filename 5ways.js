// ref: https://www.d3-graph-gallery.com/graph/scatter_basic.html

// set the dimensions and margins of the graph
let margin = {top: 15, right: 0, bottom: 50, left: 50};
let legWidth = 200
let width = 500 + legWidth - margin.left - margin.right;
let height = 500 - margin.top - margin.bottom;

// append the svg object to the body of the page
let svg = d3.select('#d3_viz')
  	.append('svg')
		.attr('width', width + margin.left + margin.right)
		.attr('height', height + margin.top + margin.bottom)
	.append('g')
		.attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');


data = d3.csv('./cars-sample.csv').then(data => {
	data = data.filter(d => d['MPG'] != 'NA'); //filter out entries with "NA" for MPG (causes problems otherwise)

	// X axis
	wMin = Math.min.apply(Math, data.map(d => d['Weight']));
	wMax = Math.max.apply(Math, data.map(d => d['Weight']));
	let x = d3.scaleLinear()
		.domain([wMin - 100, wMax + 100])
		.range([0, width - legWidth]);
  	
	svg.append('g')
		.attr('transform', 'translate(0,' + height + ')')
		.call(d3.axisBottom(x));

  	// Y axis
	mpgMin = Math.min.apply(Math, data.map(d => d['MPG']));
	mpgMax = Math.max.apply(Math, data.map(d => d['MPG']));
	let y = d3.scaleLinear()
		.domain([mpgMin - 5, mpgMax + 5])
		.range([height, 0]);
  	
	svg.append('g')
		.call(d3.axisLeft(y));

		
	// Dot sizing
	let size = d3.scaleLinear()
		.domain([1500, 5000])
		.range([2, 10]);


	// Colors (ref: https://observablehq.com/@d3/scatterplot-with-shapes)
	manus = data.map(d => d['Manufacturer'])
		.filter((value, index, self) => self.indexOf(value) === index);

	color = d3.scaleOrdinal(manus, d3.schemeTableau10);

	// dots
	let tooltip = d3.select('body') //ref: http://bl.ocks.org/biovisualize/1016860
	  .append('div')
	  .style('position', 'absolute')
	  .style('visibility', 'hidden')
	  .style('border', '1px solid black')
	  .style('background-color', 'white');

	svg.append('g')
		.selectAll('dot')
		.data(data)
		.enter()
		.append('circle')
			.attr('cx', d => x(d['Weight']) )
			.attr('cy', d => y(d['MPG']) )
			.attr('r', d => size(d['Weight']))
			.attr('opacity', 0.5)
			.attr('fill', d => color(d['Manufacturer']))
			.on('mouseover', function(d, i) {
				d3.select(this).attr('opacity', 1);
								
				let tip = 'Manufacturer: ' + i['Manufacturer'] + "<br>Model: 19" + i['Model.Year'] + " " + i['Car'] + '<br>Weight: ' + i['Weight'] + '<br>MPG: ' + i['MPG'];

				return tooltip.html(tip).style('visibility', 'visible');
			})
			.on('mousemove', d => tooltip.style('top', (d.pageY+20)+'px').style('left',(d.pageX-60)+'px')) 
			.on('mouseout', function() {
				tooltip.style('visibility', 'hidden');
				d3.select(this).attr('opacity', 0.5);
			});


	// axis labels
	svg.append("text")             
      .attr("transform", "translate(" + ((width - legWidth) / 2) + " ," + (height + margin.top + 20) + ")")
      .style("text-anchor", "middle")
      .text("Weight");

	svg.append("text")
	.attr("transform", "rotate(-90)")
	.attr("y", 0 - margin.left)
	.attr("x",0 - (height / 2))
	.attr("dy", "1em")
	.style("text-anchor", "middle")
	.text("MPG");      



	// Legend (ref: https://www.d3-graph-gallery.com/graph/custom_legend.html)
	svg.append('text')
		.attr('x', 495)
		.attr('y', margin.top + 50)
		.text('Manufacturer')
		.attr('text-anchor', 'left')
   	.style('alignment-baseline', 'middle')
		.attr('font-weight', 'bold');

	svg.selectAll('manu_dots')
  		.data(manus)
  		.enter()
  		.append('circle')
    		.attr('cx', width - legWidth + 50)
    		.attr('cy', (d, i) => margin.top + 75 + i*25) // 100 is where the first dot appears. 25 is the distance between dots
    		.attr('r', 5)
			.attr('opacity', 0.5)
    		.style('fill', d => color(d));

	svg.selectAll('manu_labels')
  		.data(manus)
  		.enter()
  		.append('text')
   		.attr('x', width - legWidth + 60)
   		.attr('y', (d,i) => margin.top + 76 + i*25) // 100 is where the first dot appears. 25 is the distance between dots
   		.text(d => d)
   		.attr('text-anchor', 'left')
   		.style('alignment-baseline', 'middle');

	svg.append('text')
		.attr('x', width - legWidth + 40)
		.attr('y', 250)
		.text('Weight')
		.attr('text-anchor', 'left')
		.style('alignment-baseline', 'middle')
		.attr('font-weight', 'bold');

	svg.selectAll('weight_dots')
		.data([2000, 3000, 4000])
		.enter()
		.append('circle')
		  	.attr('cx', width - legWidth + 50)
		  	.attr('cy', (d, i) => 275 + i*25) // 100 is where the first dot appears. 25 is the distance between dots
		  	.attr('r', d => size(d))
			.attr('opacity', 0.5)
		  	.style('fill', 'gray')
			.style('stroke', 'black');

	svg.selectAll('weight_labels')
  		.data([2000, 3000, 4000])
  		.enter()
  		.append('text')
   		.attr('x', width - legWidth + 65)
   		.attr('y', (d,i) => 277 + i*25) // 100 is where the first dot appears. 25 is the distance between dots
   		.text(d => d)
   		.attr('text-anchor', 'left')
   		.style('alignment-baseline', 'middle');
});
