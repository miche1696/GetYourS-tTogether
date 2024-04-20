const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

// Import routes
const authRoutes = require('./routes/authRoutes');
const habitRoutes = require('./routes/habitRoutes');
const userRoutes = require('./routes/userRoutes');

// Import middleware
const errorMiddleware = require('./middleware/errorMiddleware');

const app = express();

// Connect to MongoDB ----------- TO DO : replace 'mongodb://localhost:27017/habitTracker' with the actual URI of your MongoDB instance and fill in the actual logic in your route handlers and middleware.
mongoose.connect('mongodb://localhost:27017/habitTracker', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Middlewares
app.use(cors()); // Enable CORS
app.use(bodyParser.json()); // Parse JSON bodies

// Use routes
app.use('/api/auth', authRoutes);
app.use('/api/habits', habitRoutes);
app.use('/api/users', userRoutes);

// Error handling middleware
app.use(errorMiddleware);

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

module.exports = app;