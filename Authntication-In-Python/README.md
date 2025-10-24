# Authentication in Python

A simple Flask-based user authentication system with registration, login, and dashboard features. This project demonstrates secure user management using Flask, SQLAlchemy, and bcrypt for password hashing.

## Features

- **User Registration**: Secure registration with server-side validation for name, email, and password.
- **User Login**: Authenticated login with session management.
- **Dashboard**: Protected dashboard accessible only to logged-in users.
- **Logout**: Secure logout functionality.
- **Password Security**: Passwords are hashed using bcrypt.
- **Input Validation**: Both client-side and server-side validation for forms.
- **Flash Messages**: User feedback for actions like successful registration or login errors.
- **Modern UI**: Responsive design with CSS animations and gradients.

## Technologies Used

- **Flask**: Web framework for Python.
- **Flask-SQLAlchemy**: ORM for database interactions.
- **bcrypt**: For secure password hashing.
- **SQLite**: Database for storing user data.
- **HTML/CSS/JavaScript**: For frontend templates and styling.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/authentication-python.git
   cd authentication-python
   ```

2. **Install dependencies**:
   Make sure you have Python installed. Then run:
   ```bash
   pip install flask flask-sqlalchemy bcrypt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the app**:
   Open your browser and go to `http://127.0.0.1:5000/`

## Usage

- **Registration**: Visit `/reg` to create a new account. Provide a name (at least 3 characters), a valid email, and a password (at least 8 characters with at least one letter and one number).
- **Login**: Visit `/login` to log in with your email and password.
- **Dashboard**: After logging in, you'll be redirected to the dashboard.
- **Logout**: Click the logout link to end your session.

## Project Structure

```
authentication-python/
├── app.py                 # Main Flask application
├── README.md              # Project documentation
├── instance/
│   └── site.db            # SQLite database
├── static/
│   └── styles.css         # CSS styles for the UI
└── templates/
    ├── reg.html           # Registration page
    ├── login.html         # Login page
    └── dashboard.html     # User dashboard
```

## Security Features

- Password hashing with bcrypt.
- Session-based authentication.
- Input sanitization and validation.
- Protection against common vulnerabilities like SQL injection via SQLAlchemy.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.



