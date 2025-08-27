import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Notes = () => {
    const [notes, setNotes] = useState([]);
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [editingNoteId, setEditingNoteId] = useState(null);

    useEffect(() => {
        fetchNotes();
    }, []);

    const fetchNotes = async () => {
        const response = await axios.get('/api/notes');
        setNotes(response.data);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (editingNoteId) {
            await axios.put(`/api/notes/${editingNoteId}`, { title, content });
        } else {
            await axios.post('/api/notes', { title, content });
        }
        setTitle('');
        setContent('');
        setEditingNoteId(null);
        fetchNotes();
    };

    const handleEdit = (note) => {
        setTitle(note.title);
        setContent(note.content);
        setEditingNoteId(note._id);
    };

    const handleDelete = async (id) => {
        await axios.delete(`/api/notes/${id}`);
        fetchNotes();
    };

    return (
        <div className="p-4">
            <h2 className="text-2xl font-bold mb-4">Notes</h2>
            <form onSubmit={handleSubmit} className="mb-4">
                <input
                    type="text"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    placeholder="Title"
                    className="border p-2 mr-2"
                    required
                />
                <textarea
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                    placeholder="Content"
                    className="border p-2 mr-2"
                    required
                />
                <button type="submit" className="bg-blue-500 text-white p-2">
                    {editingNoteId ? 'Update Note' : 'Add Note'}
                </button>
            </form>
            <ul>
                {notes.map((note) => (
                    <li key={note._id} className="border-b py-2">
                        <h3 className="font-semibold">{note.title}</h3>
                        <p>{note.content}</p>
                        <button onClick={() => handleEdit(note)} className="text-blue-500 mr-2">
                            Edit
                        </button>
                        <button onClick={() => handleDelete(note._id)} className="text-red-500">
                            Delete
                        </button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Notes;