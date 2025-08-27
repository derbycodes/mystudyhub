import React from 'react';

const Dashboard = () => {
    const subjects = [
        { name: 'Mathematics', hours: 10 },
        { name: 'Physics', hours: 8 },
        { name: 'Chemistry', hours: 12 },
        { name: 'Biology', hours: 6 },
    ];

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Study Dashboard</h1>
            <div className="bg-white shadow-md rounded-lg p-6">
                <h2 className="text-xl font-semibold mb-2">Subjects and Hours</h2>
                <table className="min-w-full">
                    <thead>
                        <tr className="bg-gray-200">
                            <th className="py-2 px-4 text-left">Subject</th>
                            <th className="py-2 px-4 text-left">Hours Spent</th>
                        </tr>
                    </thead>
                    <tbody>
                        {subjects.map((subject, index) => (
                            <tr key={index} className="border-b">
                                <td className="py-2 px-4">{subject.name}</td>
                                <td className="py-2 px-4">{subject.hours}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
            <div className="mt-6">
                <h2 className="text-xl font-semibold mb-2">Notes Section</h2>
                <textarea
                    className="w-full h-32 border rounded-lg p-2"
                    placeholder="Write your notes here..."
                ></textarea>
                <button className="mt-2 bg-blue-500 text-white py-2 px-4 rounded">
                    Save Note
                </button>
            </div>
        </div>
    );
};

export default Dashboard;