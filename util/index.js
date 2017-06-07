var mysql = require('mysql');
var fs = require("fs");
var buf = new Buffer(1024);


//递归删除文件夹
deleteFolderRecursive = function(path) {
    var files = [];
    if( fs.existsSync(path) ) {
        files = fs.readdirSync(path);
        files.forEach(function(file,index){
            var curPath = path + "/" + file;
            if(fs.statSync(curPath).isDirectory()) { // recurse
                deleteFolderRecursive(curPath);
            } else { // delete file
                fs.unlinkSync(curPath);
                console.log('已删除文件：'+curPath)
            }
        });
        fs.rmdirSync(path);
    }else{
        console.error('目录不存在:'+path)
    }
};

//递归清空文件夹下所有内容
emptyFoldersFilesRecursive = function(path){
    var files = [];
    if( fs.existsSync(path) ) {
        files = fs.readdirSync(path);
        files.forEach(function(file,index){
            var curPath = path + "/" + file;
            if(fs.statSync(curPath).isDirectory()) { // recurse
                deleteFolderRecursive(curPath);
            } else { // delete file
                fs.unlinkSync(curPath);
                console.log('已删除文件：'+curPath)
            }
        });
    }else{
        console.error('目录不存在:'+path)
    }
}

//向指定位置写入文件
writeTextFileToPath=function(path,text){
    fs.writeFile(path, text, {flag: 'w'}, function (err) {
       if(err) {
        console.error(err);
        } else {
           console.log('写入成功');
        }
    });
}
// writeTextFileToPath('tets2.txt','tysdkhfjgjdshfg')



var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : '18516340862',
  database : 'mkalexData'
});
connection.connect();


let portfolios;

connection.query('SELECT * FROM mkalexData.webPage_portfolio',
function (error, results, fields) {
  if (error) throw error;
  portfolios=results
  // console.log(portfolios)

  portfolios.forEach((port)=>{
      writeTextFileToPath(port.name+'.md',port.content);
  })

});
