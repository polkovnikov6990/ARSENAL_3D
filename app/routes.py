from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/structure')
def structure():
    return render_template('structure.html')

if __name__ == '__main__':
    app.run(debug=True)
