const express = require('express')
const app = express();
const port = 8000;
const path = require('path')

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname + '/index.html'));
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}!`)
});


// d3.csv("../cars-sample.csv")
//     .row(function(d) { return {key: d.key, value: +d.value}; })
//     .get(function(error, rows) { console.log(rows); });