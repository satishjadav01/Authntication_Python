from flask import Flask, request, render_template, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import re
app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
   
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
    
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect(url_for('reg'))

@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Server-side validations
        if not name or len(name.strip()) < 3:
            flash('Name must be at least 3 characters long.')
            return redirect(url_for('reg'))

        if not email or not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email):
            flash('Please enter a valid email address.')
            return redirect(url_for('reg'))

        # Medium level password validation: min 8 chars, at least one letter and one number
        if not password or not re.match(r'^(?=.*[A-Za-z])(?=.*\d).{8,}$', password):
            flash('Password must be at least 8 characters long and include at least one letter and one number.')
            return redirect(url_for('reg'))

        existing_user = user.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please log in.')
            return redirect(url_for('login'))
        new_user = user(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('reg.html')
              
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Server-side validations
        if not email or not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email):
            flash('Please enter a valid email address.')
            return redirect(url_for('login'))

        if not password:
            flash('Please enter your password.')
            return redirect(url_for('login'))

        user_obj = user.query.filter_by(email=email).first()
        if user_obj and user_obj.check_password(password):
            session['user_id'] = user_obj.id
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials.')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
