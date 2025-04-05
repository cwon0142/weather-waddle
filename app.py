from config import app
from flask import render_template

@app.route('/')
def index():
    return 'Welcome to Weather Waddle!'


if __name__ == '__main__':
    app.run()