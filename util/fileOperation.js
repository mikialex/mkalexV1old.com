var fs = require("fs");

//递归删除文件夹
exports.deleteFolderRecursive = function(path) {
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
exports.emptyFoldersFilesRecursive = function(path){
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
exports.writeTextFileToPath=function(path,text){
    // fs.writeFile(path, text, {flag: 'w'}, function (err) {
    //    if(err) {
    //     console.error(err);
    //     } else {
    //        console.log('写入成功:'+path);
    //     }
    // });
    console.log('写入文件：'+path)
    fs.writeFileSync(path, text, 'utf8')
}
// writeTextFileToPath('tets2.txt','tysdkhfjgjdshfg')
