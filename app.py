from flask import Flask, render_template, redirect, url_for, request, flash
from forms import RegistrationForm, LoginForm, StudyGoalForm, NoteForm
from models import db, User, StudyGoal, Note
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from flask_login import LoginManager, current_user, login_required, login_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Ensures @login_required redirects to login

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose another.', 'danger')
            return render_template('register.html')
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    goals = StudyGoal.query.filter_by(user_id=current_user.id).all()
    user_notes = Note.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', notes=user_notes, goals=goals)

@app.route('/add_goal', methods=['POST'])
@login_required
def add_goal():
    subject = request.form['subject']
    hours_spent = request.form['hours_spent']
    new_goal = StudyGoal(subject=subject, hours_spent=hours_spent, user_id=current_user.id)
    db.session.add(new_goal)
    db.session.commit()
    flash('Study goal added!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/add_note', methods=['POST'])
@login_required
def add_note():
    content = request.form['content']
    topic = request.form['topic']
    new_note = Note(content=content, topic=topic, user_id=current_user.id)
    db.session.add(new_note)
    db.session.commit()
    flash('Note added!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/delete_note/<int:note_id>', methods=['POST'])
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.user_id != current_user.id:
        flash('You are not authorized to delete this note.', 'danger')
        return redirect(url_for('dashboard'))
    db.session.delete(note)
    db.session.commit()
    flash('Note deleted!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)