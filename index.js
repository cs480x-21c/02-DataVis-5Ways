const express = require('express')
const app = express();
const port = 8000;
const path = require('path')

app.use(express.static('./'))
app.use(express.static('./d3/'))
app.use(express.static('./matplotlib/'))

// app.get('/matplotlib/index.php', (req, res) => {
//     res.sendFile(path.join(__dirname + '/matplotlib/index.php'));
// });

app.listen(port, () => {
  console.log(`Example app listening on port ${port}!`)
});

