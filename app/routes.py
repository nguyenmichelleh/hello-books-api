from app import db
from app.models.book import Book
from flask import Blueprint, request, make_response
from flask import jsonify

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET", "POST"], strict_slashes=False)
def handle_books():
    if request.method == "GET":
        
        title_query = request.args.get("title") # returns None if query param not found
        if title_query:
            books = Book.query.filter_by(title=title_query) # if we have a param filter results by it
        else:
            books = Book.query.all()

        books_response = []
        for book in books:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
            })
        return jsonify(books_response)

    elif request.method == "POST":

        request_body = request.get_json()
        new_book = Book(title=request_body["title"],
                        description=request_body["description"])
        db.session.add(new_book)
        db.session.commit()

        return {
            "success": True,
            "message": f"Book {new_book.title} has been created"
            }

    # return make_response(f"Book {new_book.title} successfully created", 201)

@books_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"])
def handle_book(book_id):
    book = Book.query.get(book_id)

    if book is None:
        return make_response("The book you've selected could not be found.", 404)

    if request.method == "GET":
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }

        
        # if book... 
        # return {
        #     "message": "I couldn't find that book.",
        #     "success": False,
        # }, 404

        # Learn code:
        # if book is None:
        #    return make_response("Err message here", 404)
        # return {
        #     "id": xxx}

    elif request.method == "PUT":
        form_data = request.get_json()

        book.title = form_data["title"]
        book.description = form_data["description"]

        # can we use session.add here or only for new instances?
        db.session.commit()

        return make_response(f"Book {book.id} successfully updated.")
    
    elif request.method == "DELETE":

        db.session.delete(book)
        db.session.commit()

        return make_response(f"Book {book.id} successfully deleted.") # can id's re-order themselves?
