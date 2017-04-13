var http = require('http');

var opts = {
    hostname: 'jsonplaceholder.typicode.com',
    method: 'DELETE',
    path: '/posts/1'
};
var req = http.request(opts, (res) => {
    var body = '';
    res.on('data', (chunk) => {
        body += chunk;
    });
    res.on('end', () => {
        console.log(body);
    });
});
req.on('error', (e) => {
    console.error(e);
});
req.end();
