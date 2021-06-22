from flask import Flask, render_template

app = Flask(__name__)
# app = Flask(__name__, template_folder='template')  # still relative to module

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/more')
def more():
    return render_template("more.html")

