/**
 * main.js
 * date created: 2/09/2021
 * Author: Benjamin M'Sadoques
 *
 * Provides the main method to load the data then build the vis
 */

/**
 * the main method for loading the data and building the vis
 */
function main()
{
    // Waits till the data is read
    let dataPromise = new Promise((resolve)=>
    {
        let data = d3.csv("./cars-sample.csv", function(d)
        {
            // filter out when MPG is NA
            if (d.MPG !== "NA")
            {
                return d;
            }
        })
        resolve(data);
    });

    // Runs only after the file is parsed
    dataPromise.then(function(data) { d3Main(data); })
}