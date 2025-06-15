# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the main HTML page for the JSON/XML editor.
    """
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask application in debug mode for development.
    # In a production environment, you would use a WSGI server like Gunicorn.
    app.run(debug=False)
