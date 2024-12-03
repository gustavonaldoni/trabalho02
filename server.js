const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

const FLASK_URL = 'http://localhost:5000/encrypt';

app.post('/encrypt-message', async (req, res) => {
    try {
        const { message } = req.body;

        if (!message) {
            return res.status(400).json({ error: "Missing 'message'" });
        }

        const response = await axios.post(FLASK_URL, { message });

        res.json(response.data);
    } catch (error) {
        console.error(error.message);
        res.status(500).json({ error: 'Failed to encrypt message' });
    }
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Node.js server running on http://localhost:${PORT}`);
});
