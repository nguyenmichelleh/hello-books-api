from app import db
# db is instance of SQLAlchemy

# "Book is a MODEL, with these three columns"
# SQLAlchemy wants singular class names
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)

    # __tablename__ = "books" would change the class name, singular to table, plural
    # can define funtions in here