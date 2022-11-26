from flask import Flask
from flask import render_template
from flask import request
import json
import requests
import secrets

app = Flask(__name__)

# セッション情報を暗号化するためのキー設定
app.secret_key = secrets.token_urlsafe(32)


@app.route("/")
def hello():
    return render_template("index1.html")


@app.route("/index2")
def index2():

    return render_template("index2.html")


# @app.route("/", methods=["GET", "POST"])
# def redirect_to_page():
#      if request.method == "POST":
#          if "file" not in request.files:
#              flash("ファイルが選択されていません")
#              return redirect(request.url)
#          if a = "姫待不動尊"
#             return redirect("index2.html")

@app.route("/index3")
def index3():
    
    return render_template("index3.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
