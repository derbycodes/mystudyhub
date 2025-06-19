# My Study Hub

My Study Hub is a web application designed to help students track their study sessions, set goals, and manage their notes effectively. The application is built using Flask for the backend and Tailwind CSS for the frontend, ensuring a responsive and visually appealing user experience.

## Features

- User authentication (Login/Register)
- Dashboard for tracking study subjects and hours spent
- Ability to set and manage study goals
- Notes section for creating, reading, updating, and deleting notes
- Responsive design using Tailwind CSS

## Project Structure

```
my-study-hub
├── backend
│   ├── app.py                # Main entry point for the Flask application
│   ├── models.py             # Database models using SQLAlchemy
│   ├── forms.py              # Forms for user registration, login, and study goals
│   ├── database.db           # SQLite database file
│   ├── requirements.txt       # Python dependencies
│   └── README.md             # Documentation for the backend
├── frontend
│   ├── public
│   │   ├── index.html        # Homepage of the application
│   │   ├── login.html        # Login form
│   │   ├── register.html     # Registration form
│   │   ├── dashboard.html     # User dashboard
│   │   ├── notes.html        # Notes management
│   │   └── styles
│   │       ├── main.css      # Custom CSS styles
│   │       └── tailwind.css  # Tailwind CSS framework
│   └── README.md             # Documentation for the frontend
└── README.md                 # Overview of the entire project
```

## Setup Instructions

### Backend

1. Navigate to the `backend` directory.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```
   python app.py
   ```

### Frontend

1. Navigate to the `frontend/public` directory.
2. Open `index.html` in your web browser to view the application.

## Usage

- Register a new account or log in to access your dashboard.
- Track your study hours and set goals for each subject.
- Manage your notes in the dedicated notes section.

## Contributing

Feel free to contribute to the project by submitting issues or pull requests. Your feedback and suggestions are welcome!