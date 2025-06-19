from flask import Flask, render_template, redirect, url_for, request, flash, session
from forms import RegistrationForm, LoginForm, StudyGoalForm, NoteForm
from models import db, User, StudyGoal, Note  # Import db from models.py
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)  # Initialize db with app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))  # Redirects to dashboard
        else:
            flash('Login failed. Check username and password.', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose another.', 'danger')
            return render_template('register.html')
        # Create new user
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    goals = StudyGoal.query.filter_by(user_id=session['user_id']).all()
    notes = Note.query.filter_by(user_id=session['user_id']).all()
    return render_template('dashboard.html', goals=goals, notes=notes)

@app.route('/add_goal', methods=['POST'])
def add_goal():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    subject = request.form['subject']
    hours_spent = request.form['hours_spent']
    # Save to database
    new_goal = StudyGoal(subject=subject, hours_spent=hours_spent, user_id=session['user_id'])
    db.session.add(new_goal)
    db.session.commit()
    flash('Study goal added!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/add_note', methods=['POST'])
def add_note():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    content = request.form['content']
    new_note = Note(content=content, user_id=session['user_id'])
    db.session.add(new_note)
    db.session.commit()
    flash('Note added!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)