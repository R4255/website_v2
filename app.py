from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "Hello world and how are you"


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
