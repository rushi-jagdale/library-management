from flask import Blueprint, request, jsonify
from db import get_db_connection

library_routes = Blueprint("library", __name__)

# CRUD for Books
@library_routes.route("/books", methods=["GET", "POST"])
def books():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "GET":
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        conn.close()
        return jsonify(books)

    if request.method == "POST":
        data = request.json
        cursor.execute(
            "INSERT INTO books (title, author, published_year) VALUES (%s, %s, %s)",
            (data["title"], data["author"], data["published_year"]),
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Book added successfully"}), 201


@library_routes.route("/books/<int:id>", methods=["GET", "PUT", "DELETE"])
def book_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "GET":
        cursor.execute("SELECT * FROM books WHERE id = %s", (id,))
        book = cursor.fetchone()
        conn.close()
        if book:
            return jsonify(book)
        return jsonify({"error": "Book not found"}), 404

    if request.method == "PUT":
        data = request.json
        cursor.execute(
            "UPDATE books SET title = %s, author = %s, published_year = %s WHERE id = %s",
            (data["title"], data["author"], data["published_year"], id),
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Book updated successfully"})

    if request.method == "DELETE":
        cursor.execute("DELETE FROM books WHERE id = %s", (id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Book deleted successfully"})


# CRUD for Members
@library_routes.route("/members", methods=["GET", "POST"])
def members():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "GET":
        cursor.execute("SELECT * FROM members")
        members = cursor.fetchall()
        conn.close()
        return jsonify(members)

    if request.method == "POST":
        data = request.json
        cursor.execute(
            "INSERT INTO members (name, email, phone) VALUES (%s, %s, %s)",
            (data["name"], data["email"], data["phone"]),
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Member added successfully"}), 201


@library_routes.route("/members/<int:id>", methods=["GET", "PUT", "DELETE"])
def member_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "GET":
        cursor.execute("SELECT * FROM members WHERE id = %s", (id,))
        member = cursor.fetchone()
        conn.close()
        if member:
            return jsonify(member)
        return jsonify({"error": "Member not found"}), 404

    if request.method == "PUT":
        data = request.json
        cursor.execute(
            "UPDATE members SET name = %s, email = %s, phone = %s WHERE id = %s",
            (data["name"], data["email"], data["phone"], id),
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Member updated successfully"})

    if request.method == "DELETE":
        cursor.execute("DELETE FROM members WHERE id = %s", (id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Member deleted successfully"})
