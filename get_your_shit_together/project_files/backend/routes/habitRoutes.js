const express = require('express');
const router = express.Router();
const habitController = require('../controllers/habitController');

// Define the routes and associate them with controller methods
router.post('/', habitController.createHabit);
router.get('/', habitController.getAllHabits);
router.get('/:id', habitController.getHabitById);
router.put('/:id', habitController.updateHabit);
router.delete('/:id', habitController.deleteHabit);

module.exports = router;