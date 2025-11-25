// routes/rankingRoutes.js

const express = require('express');
const router = express.Router();
const rankingController = require('../controllers/rankingController');

// Define a rota GET para /ranking
router.get('/', rankingController.getRankingPage);

module.exports = router;