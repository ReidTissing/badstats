

const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');
const scriptPath = "./app.py";
// const d3 = require('d3');
const { exec } = require('child_process');
const csv = require('csvtojson');
var app = require('express')();
app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));
app.set('view engine', 'ejs')

const csvs = ['presweight','serialkillers'].map(csvname => csvname+'.csv');
function getCsvData (csvName) {
  return csv().fromFile(csvName);
};


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

app.get('/stats', async function(req, res) {
//get csv data to work with
  const serialkillers = await getCsvData('serialkillers.csv');
  // console.log(JSON.stringify(csvdata))
  //output array elements from csv
  console.log(serialkillers[1].name);
  execPythonScript((output, error) => {
    if (error) {
      res.status(500).send({ error: `Something fucking went wrong. ${error}` })
    } else {
      res.json({ message: output });
    }
  })
});