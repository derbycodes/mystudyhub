# My Study Hub Backend

## Overview
My Study Hub is a web application designed to help users track their study subjects and hours spent, along with a note section for managing study materials. This backend documentation provides an overview of the setup and API endpoints available for the application.

## Features
- User authentication (login and registration)
- Create, read, update, and delete notes
- Optional features for uploading PDFs or links to study materials

## Technologies Used
- Node.js
- Express.js
- MongoDB (or any other database of your choice)
- JWT for authentication

## Setup Instructions

### Prerequisites
- Node.js installed on your machine
- MongoDB (or any other database) set up and running

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-study-hub/backend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Create a `.env` file in the root of the backend directory and add your environment variables:
   ```
   PORT=5000
   MONGODB_URI=<your-mongodb-uri>
   JWT_SECRET=<your-jwt-secret>
   ```

4. Start the server:
   ```
   npm start
   ```

## API Endpoints

### Authentication
- **POST /api/auth/register**: Register a new user
- **POST /api/auth/login**: Login an existing user

### Notes
- **GET /api/notes**: Retrieve all notes for the authenticated user
- **POST /api/notes**: Create a new note
- **PUT /api/notes/:id**: Update an existing note
- **DELETE /api/notes/:id**: Delete a note

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.