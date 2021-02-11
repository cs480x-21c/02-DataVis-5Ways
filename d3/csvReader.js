function main()
{
    // some code ideas from https://www.d3-graph-gallery.com/scatter

    // Waits till the data is read
    let dataPromise = new Promise((resolve)=>
    {
        let data = d3.csv("./cars-sample.csv", function(d)
        {
            return d;
        })
        resolve(data);
    });

    dataPromise.then(
        function(data)
        {
            // pixel size taken from the image provided (exact)
            const width = 616;
            const height = 439;

            const margin = {top: 8, bottom: 41, left: 53, right: 111};
            const plot = {width: 452, height: 390};

            let svg = d3.select('#vis')
                .attr('width', width)
                .attr('width', height)

            // the scales are linear, but start and end at non-zero
            let xScale = d3.scaleLinear()
                .domain([1500, 5100])   // 1500, is true; 5100 is an estimate
                .range([margin.left, margin.left + plot.width]);      // measurements taken from the picture

            let yScale = d3.scaleLinear()
                .domain([5.666666, 45.666666])   // measurements taken from the picture
                .range([margin.bottom + plot.height, margin.bottom]);                 // measurements taken from the picture

            svg.append("g")
                .attr("transform", "translate(" + margin.left + ",0)")
                .call(d3.axisLeft(yScale)
                    .tickValues(10, 20, 30, 40));


            let rScale = d3.scaleLinear()
                .domain([1500, 5100])
                .range([0, 10]);                        // measurements estimated from the picture

            let cScale = d3.scaleOrdinal()
                .domain(["bmw", "ford", "honda", "mercedes", "toyota"])
                .range(["#f1b2af7F","#c7c8877F", "#8ed4b67F", "#8dcef07F", "#e9acee7F"]) // Colors taken from the picture, Opacity was specified to be half

            svg.append('g')
                .selectAll("dot")
                .data(data)
                .enter()
                .append("circle")
                .attr("cx", function(d) { return xScale(d.Weight)})
                .attr("cy", function(d) { return yScale(d.MPG)})
                .attr("r", function(d) { return rScale(d.Weight) })
                .style("fill", function(d) { return cScale(d.Manufacturer)})
        }
    )
}