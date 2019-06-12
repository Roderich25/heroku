import time
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/posts", methods=["POST"])
def posts():
    # start and end point for posts
    start = int(request.form.get("start") or 0)
    end = int(request.form.get("end") or (start + 9))

    # list of posts
    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    # simulate delay of response
    time.sleep(1)

    # return list of posts
    return jsonify(data)


if __name__ == '__main__':
    app.run()
