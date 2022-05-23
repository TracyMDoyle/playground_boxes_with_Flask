from turtle import color
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/play")
def play():
    return render_template("play.html", num_boxes=3, color="blue")

@app.route("/play/<int:num_boxes>")
def playground(num_boxes):
    return render_template("play.html", num_boxes = num_boxes, color="blue")

@app.route("/play/<int:num_boxes>/<string:color>")
def playground_color(num_boxes, color):
    return render_template("play.html", num_boxes = num_boxes, color = color)


if __name__ =="__main__":
    app.run(debug=True, port=5001)