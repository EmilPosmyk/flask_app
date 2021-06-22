from flask import Flask

app = Flask(__name__)
# app = Flask(__name__, template_folder='template')  # still relative to module

@app.route('/')
def hello_world():
    return 'Hello World!'

