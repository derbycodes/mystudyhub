const express = require('express');
const router = express.Router();
const notesController = require('../controllers/notesController');
const authMiddleware = require('../middleware/authMiddleware');

// Route to create a new note
router.post('/', authMiddleware, notesController.createNote);

// Route to get all notes for a user
router.get('/', authMiddleware, notesController.getNotes);

// Route to update a note by ID
router.put('/:id', authMiddleware, notesController.updateNote);

// Route to delete a note by ID
router.delete('/:id', authMiddleware, notesController.deleteNote);

module.exports = router;