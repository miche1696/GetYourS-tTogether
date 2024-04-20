const mongoose = require('mongoose');

// Define the schema for a habit
const habitSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  description: String,
  frequency: {
    type: String,
    required: true,
  },
  startDate: {
    type: Date,
    default: Date.now,
  },
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
  },
  // Add more fields as necessary
});

// Create the model from the schema
const Habit = mongoose.model('Habit', habitSchema);

module.exports = Habit;