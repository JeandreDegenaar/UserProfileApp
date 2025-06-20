"""
/**
 * File: forms.py
 *
 * Purpose:
 * Defines Flask-WTF form classes for user registration and update forms.
 * Includes validation logic to ensure data integrity, such as email format,
 * string length, and numeric range checks.
 *
 * Features:
 * - RegistrationForm: used for creating new users with validation
 * - UpdateForm: inherits from RegistrationForm but with a different submit button
 * - Custom validator: NotOnlyWhitespace to reject blank or space-only input
 */
"""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Email, Length, NumberRange, ValidationError

# Custom validator to prevent only-whitespace inputs
def NotOnlyWhitespace(form, field):
    if not field.data or not field.data.strip():
        raise ValidationError('This field cannot be empty or just spaces.')

# Form used for registering a new user
class RegistrationForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[
            NotOnlyWhitespace,
            Length(min=2, max=50, message="Name must be between 2 and 50 characters.")
        ]
    )
    email = StringField(
        'Email',
        validators=[
            NotOnlyWhitespace,
            Email(message="Enter a valid email address.")
        ]
    )
    age = IntegerField(
        'Age',
        validators=[
            NumberRange(min=0, max=120, message="Age must be between 0 and 120.")
        ]
    )
    submit = SubmitField('Register')  # Button label for registration

# Form used for updating existing users (inherits all fields from RegistrationForm)
class UpdateForm(RegistrationForm):
    submit = SubmitField('Update')  # Overridden submit label for update

# Form used for deleting a user (used only to hold CSRF token)
class DeleteForm(FlaskForm):
    pass
