from app import app, db

# Run this in the Flask app context
with app.app_context():
    db.create_all()
    print("Database created.")
