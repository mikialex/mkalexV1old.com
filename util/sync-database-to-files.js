'use strict';

//sync database to files

var fileio=require('./fileOperation.js');

var mysql = require('mysql');
var fs = require("fs");

var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : '18516340862',
  database : 'mkalexData'
});
connection.connect();

let isPortOver=false;
let isPostOver=false;
function checkIsOver(){
    if(isPortOver&&isPostOver){process.exit()}
}
let portfolios;
let articles;

const disPortPath='../word/portfolios'
const disPostPath='../word/post'

connection.query('SELECT * FROM mkalexData.webPage_portfolio',
function (error, results, fields) {
  if (error) throw error;
  if(fs.existsSync(disPortPath)){
      fileio.deleteFolderRecursive(disPortPath)
  }
  fs.mkdirSync(disPortPath);
  portfolios=results
  // console.log(portfolios)

  portfolios.forEach((port)=>{
      fileio.writeTextFileToPath(disPortPath+'/'+port.name+'.md',port.content);
  })
  isPortOver=true;
  checkIsOver();
});

connection.query('SELECT * FROM mkalexData.webPage_article;',
function (error, results, fields) {
  if (error) throw error;
  if(fs.existsSync(disPostPath)){
      fileio.deleteFolderRecursive(disPostPath)
  }
  fs.mkdirSync(disPostPath);
  articles=results
  // console.log(portfolios)

  articles.forEach((article)=>{
      fileio.writeTextFileToPath(disPostPath+'/'+article.title+'.md',article.content);
  })

  isPostOver=true;
  checkIsOver();
});
