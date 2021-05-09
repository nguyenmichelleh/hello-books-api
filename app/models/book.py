from app import db
# db is instance of SQLAlchemy

# SQLAlchemy wants singular class names
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)

    # __tablename__ = "books" would change the class name, singular to table, plural