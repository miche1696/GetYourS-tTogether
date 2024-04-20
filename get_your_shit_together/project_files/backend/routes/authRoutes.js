const express = require('express');
const router = express.Router();
const authController = require('../controllers/authController');

// Define the routes and associate them with controller methods
router.post('/register', authController.register);
router.post('/login', authController.login);
router.post('/logout', authController.logout);

module.exports = router;