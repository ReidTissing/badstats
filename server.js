

const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');
const scriptPath = "./app.py";

const { exec } = require('child_process');

var app = require('express')();
app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));
app.set('view engine', 'ejs')

function execPythonScript(result) {
  exec(`python ${scriptPath}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`exec 3rr0r: ${error}`);
      result(undefined, error);
      return;
    }
    result(stdout, stderr);
  });
}

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}
app.listen(3000 , (err)=>{console.log('Listening')});

app.get('/' , function(req , res) {
    res.render('index' , {result_from_database: res.body} );   
});

app.get('/stats', function(req, res) {
  // var randint = getRandomInt(500);
  //    res.json({
  //      message: randint
  //    });
  execPythonScript((output, error) => {
    if (error) {
      res.status(500).send({ error: `Something fucking went wrong. ${error}` })
    } else {
      res.json({ message: output });
    }
  })
});