from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.utcnow().year
    name = 'Jose V.'
    return render_template('home.html', now = now, name = name)

if __name__ == '__main__':
    app.run(debug=True)
