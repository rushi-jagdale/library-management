from flask import Flask
from routes import library_routes
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Register blueprints
app.register_blueprint(library_routes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)