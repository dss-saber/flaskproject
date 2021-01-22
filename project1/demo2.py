from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "欢迎来到Flask首页"


@app.route("/<int:pk>")
def detail(pk):
    return f"欢迎来到Flask页面{pk}"


if __name__ == '__main__':
    app.run(host="192.168.11.34", port="8000", debug=True)
