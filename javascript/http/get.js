var http = require('http');

var req = http.get('http://google.com', (res) => {
    console.log(res.statusCode);
});
