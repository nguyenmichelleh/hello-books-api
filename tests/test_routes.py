def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }

def test_one_book_with_no_records(client):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404

def test_get_all_books(client, two_saved_books):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }, {
        "id": 2,
        "title": "Mountain Book",
        "description": "i luv 2 climb rocks"
    }]

def test_add_a_book(client):
def test_create_one_planet(client, planet_data):
    #Act
    response = client.post("/books", json=book_data)
    response_body = response.get_json()

    #Assert
    assert response.status_code == 201
    assert response_body == {
            "success": True,
            "message": f"Book {new_book.title} has been created"
            }