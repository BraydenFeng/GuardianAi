const express = require ('express');
const app = express();
const port = 3000;

app.use(express.static(__dirname));

app.get('/', (req, res) =>{ res.sendFile(__dirname + '/index.html');
});

app.get('/dashboard', (req, res) => {res.sendFile(__dirname + '/dashboard.html');
});




app.listen(port, () => {
  console.log('hi');
});
