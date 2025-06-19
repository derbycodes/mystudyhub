# My Study Hub Backend Documentation

## Overview
My Study Hub is a web application designed to help students track their study sessions, set goals, and manage notes effectively. This backend documentation provides details on how to set up and use the backend components of the application.

## Features
- User authentication (registration and login)
- Adding and tracking study goals
- Managing notes (create, read, update, delete)
- SQLite database for data storage

## Setup Instructions

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-study-hub/backend
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application
1. Set the environment variable for Flask:
   - On Windows:
     ```
     set FLASK_APP=app.py
     ```
   - On macOS/Linux:
     ```
     export FLASK_APP=app.py
     ```

2. Run the Flask application:
   ```
   flask run
   ```

3. Access the application in your web browser at `http://127.0.0.1:5000`.

## Database
The application uses SQLite for data storage. The database file is located at `backend/database.db`. The following tables are created:
- Users: Stores user information for authentication.
- StudyGoals: Stores study goals set by users.
- Notes: Stores notes created by users.

## Usage
- **User Registration**: Navigate to the registration page to create a new account.
- **User Login**: Use the login page to authenticate and access the dashboard.
- **Dashboard**: After logging in, users can view their study goals and notes.
- **Notes Management**: Users can create, read, update, and delete notes from the notes section.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.