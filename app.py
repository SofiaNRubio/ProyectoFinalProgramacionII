<<<<<<< HEAD
from flask import Flask
from routes import configure_routes

app = Flask(__name__)

if __name__ == '__main__':
=======
from flask import Flask,  render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "Hola Mundo"

@app.route("/hello/<username>")
def show_name(username):
    return render_template("index.html", username=username)


if __name__ == "__main__":
>>>>>>> f21b19b (El Eze se la come)
    app.run(debug=True)
