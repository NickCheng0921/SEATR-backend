from flask_sqlalchemy import SQLAlchemy

class Code(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), unique=True)  # Define the "code" field as a unique string with a maximum length of 255 characters
