// Middleware to handle errors
const errorMiddleware = (err, req, res, next) => {
  const status = err.status || 500;
  const message = err.message || 'Something went wrong';

  res.status(status).json({
    error: {
      message: message,
    },
  });
};

module.exports = errorMiddleware;