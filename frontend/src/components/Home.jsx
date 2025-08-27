import React from 'react';

const Home = () => {
    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
            <h1 className="text-4xl font-bold text-center text-blue-600 mb-4">Welcome to My Study Hub</h1>
            <p className="text-lg text-center text-gray-700 mb-8">
                Your personal space for tracking study subjects, hours spent, and taking notes.
            </p>
            <div className="flex space-x-4">
                <a href="/login" className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
                    Login
                </a>
                <a href="/register" className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600">
                    Register
                </a>
            </div>
        </div>
    );
};

export default Home;