from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

# Rate limit: 5 requests per minute per IP
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])

# Sample data
books = [
    {"id": 1, "title": "Book A", "genre": "mystery"},
    {"id": 2, "title": "Book B", "genre": "fantasy"},
    {"id": 3, "title": "Book C", "genre": "mystery"},
]

@app.route("/api/books", methods=["GET"])
@limiter.limit("5/minute")
def get_books():
    genre = request.args.get("genre")
    api_key = request.headers.get("x-api-key")

    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    if genre:
        result = [book for book in books if book["genre"] == genre]
        return jsonify(result)
    return jsonify(books)

@app.route("/api/books", methods=["POST"])
@limiter.limit("3/minute")
def add_book():
    api_key = request.headers.get("x-api-key")
    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    if not data or "title" not in data or "genre" not in data:
        return jsonify({"error": "Missing parameters"}), 400

    new_id = len(books) + 1
    new_book = {"id": new_id, "title": data["title"], "genre": data["genre"]}
    books.append(new_book)
    return jsonify(new_book), 201

@app.route("/")
def home():
    return '''
        <h1>Simple Book API</h1>
        <p>Try sending a GET request to <code>/api/books</code> with header <code>x-api-key</code>.</p>
    '''

if __name__ == "__main__":
    app.run(debug=True)
