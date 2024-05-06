# prompt: create a hello world web app using python with header/footer and content using flask and class function

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

if __name__ == "__main__":
  app.run()
