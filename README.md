# **Library Management System API**

This project is a RESTful API built with **Flask** that implements a **Library Management System**. It allows for CRUD (Create, Read, Update, Delete) operations on **Books** and **Members**. Additionally, it includes basic functionalities such as searching books by title/author and database pagination.


## **Setup and Installation**

### 1. **Clone the repository**
```bash
git clone https://github.com/rushi-jagdale/library-management.git
cd library-management

# Create a virtual environment
python -m venv venv
# Activate the virtual environment (Windows)
venv\Scripts\activate
# Activate the virtual environment (Mac/Linux)
source venv/bin/activate

# Install required libraries
pip install -r requirements.txt


# Run the application
After setting up your database and .env file, run the Flask application.


python app.py


# Run unit tests

python -m unittest tests.py
