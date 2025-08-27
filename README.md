# My Study Hub

My Study Hub is a web application designed to help users track their study subjects, hours spent studying, and manage their notes effectively. This project consists of a frontend built with React and Tailwind CSS, and a backend powered by Node.js and Express.

## Features

- User authentication (login and registration)
- Dashboard for tracking study subjects and hours
- Notes management (create, read, update, delete)
- Option to upload PDFs or links to study materials

## Project Structure

```
my-study-hub
├── backend
│   ├── src
│   │   ├── controllers
│   │   ├── models
│   │   ├── routes
│   │   ├── middleware
│   │   └── app.js
│   ├── package.json
│   └── README.md
├── frontend
│   ├── public
│   ├── src
│   │   ├── assets
│   │   ├── components
│   │   ├── App.jsx
│   │   ├── index.js
│   │   └── styles
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── package.json
│   └── README.md
└── README.md
```

## Getting Started

### Prerequisites

- Node.js
- npm or yarn

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-study-hub
   ```

2. Install backend dependencies:
   ```
   cd backend
   npm install
   ```

3. Install frontend dependencies:
   ```
   cd frontend
   npm install
   ```

### Running the Application

1. Start the backend server:
   ```
   cd backend
   npm start
   ```

2. Start the frontend application:
   ```
   cd frontend
   npm start
   ```

### API Endpoints

- **Authentication**
  - `POST /api/auth/login` - Login a user
  - `POST /api/auth/register` - Register a new user

- **Notes Management**
  - `GET /api/notes` - Get all notes
  - `POST /api/notes` - Create a new note
  - `PUT /api/notes/:id` - Update a note
  - `DELETE /api/notes/:id` - Delete a note

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License

This project is licensed under the MIT License.
