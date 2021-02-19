from flask import Flask, render_template, url_for, request
import searchpart

app = Flask(__name__)

@app.route("/ford/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        partOne = request.form["fpnum"]
        po = searchpart.getPartLink(partOne)
        print(po)
    return render_template("index.html")

@app.route("/search/")
def dynamic():
    return searchpart.getPartLink(partOne)

if __name__ == "__main__":
    app.run(debug = True)