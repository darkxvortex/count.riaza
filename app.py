from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    target_date = datetime(2025, 12, 31, 23, 59, 59)
    return render_template('index.html', target_date=target_date)

if __name__ == '__main__':
    app.run(debug=True)
