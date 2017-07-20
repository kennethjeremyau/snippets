var Mocha = require('mocha');

// Purging the cache allows mocha to be run multiple times per process.
function purgeRequireCache() {
  Object.keys(require.cache).forEach(function(file) {
    delete require.cache[file];
  });
}

exports.handler = function(event, context, callback) {
  purgeRequireCache();
  var mocha = new Mocha();
  mocha.addFile('tests/hooks.js');
  mocha.run(function(failures) {
    callback();
  });
};
