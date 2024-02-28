const http = require('http');

// Create HTTP server
const app = http.createServer((req, res) => {
    // Set response header
    res.writeHead(200, {'Content-Type': 'text/plain'});
    
    // Send response body
    res.end('Hello Holberton School!\n');
});

// Listen on port 1245
app.listen(1245);

// Export the app
module.exports = app;