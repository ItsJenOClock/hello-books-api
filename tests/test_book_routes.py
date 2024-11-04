
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

def test_create_one_book_in_empty_db(client):
    response = client.post("/books", json={
        "title": "Romeo and Juliet",
        "description": "tragic love story",
    })
    response_body = response.get_json()
    
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "title": "Romeo and Juliet",
        "description": "tragic love story",
    }

def test_create_one_book_with_planets_already_in_db(client, two_saved_books):
    response = client.post("/books", json={
        "title": "Romeo and Juliet",
        "description": "tragic love story",
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "id": 3,
        "title": "Romeo and Juliet",
        "description": "tragic love story",
    }
