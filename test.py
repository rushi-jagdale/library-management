import unittest
import json
from app import app

class LibraryManagementTestCase(unittest.TestCase):

    # Set up the test client
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test for creating a book
    def test_create_book(self):
        new_book = {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "published_year": 1925
        }
        response = self.app.post('/books', 
                                 data=json.dumps(new_book),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("Book added successfully", response.get_data(as_text=True))

    # Test for retrieving all books
    def test_get_books(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)
        books = json.loads(response.data)
        self.assertIsInstance(books, list)

    # Test for retrieving a specific book by ID
    def test_get_book_by_id(self):
        response = self.app.get('/books/1')  # Assuming book with ID 1 exists
        self.assertEqual(response.status_code, 200)
        book = json.loads(response.data)
        self.assertEqual(book["id"], 1)

    # Test for updating a book's information
    def test_update_book(self):
        updated_book = {
            "title": "The Great Gatsby - Revised",
            "author": "F. Scott Fitzgerald",
            "published_year": 1934
        }
        response = self.app.put('/books/1', 
                                data=json.dumps(updated_book),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Book updated successfully", response.get_data(as_text=True))

    # Test for deleting a book
    def test_delete_book(self):
        response = self.app.delete('/books/1')  # Assuming book with ID 1 exists
        self.assertEqual(response.status_code, 200)
        self.assertIn("Book deleted successfully", response.get_data(as_text=True))

    # Test for creating a member
    def test_create_member(self):
        new_member = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "1234567890"
        }
        response = self.app.post('/members', 
                                 data=json.dumps(new_member),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("Member added successfully", response.get_data(as_text=True))

    # Test for retrieving all members
    def test_get_members(self):
        response = self.app.get('/members')
        self.assertEqual(response.status_code, 200)
        members = json.loads(response.data)
        self.assertIsInstance(members, list)

    # Test for retrieving a specific member by ID
    def test_get_member_by_id(self):
        response = self.app.get('/members/1')  # Assuming member with ID 1 exists
        self.assertEqual(response.status_code, 200)
        member = json.loads(response.data)
        self.assertEqual(member["id"], 1)

    # Test for updating a member's information
    def test_update_member(self):
        updated_member = {
            "name": "John Doe Jr.",
            "email": "john.doejr@example.com",
            "phone": "0987654321"
        }
        response = self.app.put('/members/1', 
                                data=json.dumps(updated_member),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Member updated successfully", response.get_data(as_text=True))

    # Test for deleting a member
    def test_delete_member(self):
        response = self.app.delete('/members/1')  # Assuming member with ID 1 exists
        self.assertEqual(response.status_code, 200)
        self.assertIn("Member deleted successfully", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
