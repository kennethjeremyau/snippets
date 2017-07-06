var fs = require('fs');
var path = require('path');

function listFiles(dirpath, files){
  files = (files == null) ? [] : files;
  fs.readdirSync(dirpath).forEach(function(file) {
    var filepath = path.join(dirpath, file)
    files = (fs.statSync(filepath).isDirectory()) ?
      listFiles(filepath, files) :
      files.concat(filepath);
    });
  return files;
}
