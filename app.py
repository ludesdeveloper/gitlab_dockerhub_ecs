from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Ludes Developer, if you saw this, Continuous Development is success'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")