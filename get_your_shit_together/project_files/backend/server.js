const http = require('http');
const app = require('./app'); // Import the Express application

const PORT = process.env.PORT || 3000;

const server = http.createServer(app); // Create the HTTP server using the Express app

server.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});