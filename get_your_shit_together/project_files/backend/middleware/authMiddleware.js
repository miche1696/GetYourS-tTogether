const jwt = require('jsonwebtoken');

// Middleware to check if the user is authenticated
const authMiddleware = (req, res, next) => {
  try {
    const token = req.headers.authorization.split(' ')[1];
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.userData = decoded;
    next();
  } catch (error) {
    return res.status(401).json({
      message: 'Authentication failed',
    });
  }
};

module.exports = authMiddleware;