"""
Flask Web Application for User Management

This application allows users to register, view, update, and delete their profiles.
It uses Flask for routing, Flask-WTF for form handling/validation, and SQLAlchemy
for interacting with an SQLite database.

Features:
- Register new users
- View all users
- Update user data via a pre-filled form
- Delete users from the database
- Store data in SQLite database
- Form validation using Flask-WTF
"""

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, UpdateForm, DeleteForm
# Initialize Flask app and configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'devsecret'  # For CSRF protection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # SQLite DB path
db = SQLAlchemy(app)  # Database instance

from models import User  # Import the User model

@app.route('/')
def home():
    # Redirect root to registration page
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Handle user registration form
    form = RegistrationForm()
    if form.validate_on_submit():
        # Create new user from form data
        new_user = User(
            name=form.name.data,
            email=form.email.data,
            age=form.age.data
        )
        db.session.add(new_user)
        db.session.commit()
        flash('User registered successfully!', 'success')
        return redirect(url_for('view_users'))
    return render_template('register.html', form=form)

@app.route('/users')
@app.route('/users')
def view_users():
    users = User.query.all()
    delete_forms = {user.id: DeleteForm() for user in users}
    return render_template('users.html', users=users, delete_forms=delete_forms)

@app.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update(user_id):
    # Load user by ID and populate update form
    user = User.query.get_or_404(user_id)
    form = UpdateForm(obj=user)
    if form.validate_on_submit():
        # Update user data with form values
        user.name = form.name.data
        user.email = form.email.data
        user.age = form.age.data
        db.session.commit()
        flash('User updated!', 'info')
        return redirect(url_for('view_users'))
    return render_template('update.html', form=form, user=user)

@app.route('/delete/<int:user_id>', methods=['POST'])
def delete(user_id):
    # Delete a user by ID
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted.', 'warning')
    return redirect(url_for('view_users'))

if __name__ == '__main__':
    app.run(debug=True)
