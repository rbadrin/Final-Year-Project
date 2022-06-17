const express = require('express');
const app = express();
const app1 = express();
app.use(express.static('public'));
app.listen(3000);
var arguments = process.argv ;
var s = parseInt(arguments[2]);
var t = parseInt(arguments[3]);
app.set('view engine', 'ejs');

app.get('/', (req, res) => {
  s = parseInt(req.query.speed);
  t = parseInt(req.query.time);
  res.render('index',{ speed: s , time : t });
});


// app1.use(express.static('public'));
// app1.listen(3001);
// var arguments = process.argv ;
// var s = parseInt(arguments[2]);
// var t = parseInt(arguments[3]);
// app1.set('view engine', 'ejs');
//
// app1.get('/', (req, res) => {
//   s = parseInt(req.query.speed);
//   t = parseInt(req.query.time);
//   res.render('index',{ speed: s , time : t });
// });
