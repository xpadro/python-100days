from flask import Flask, render_template
import requests

app = Flask(__name__)

data = []
data_dict = {}


def _load_data():
    global data, data_dict
    data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    data_dict = {item['id']: item for item in data}


@app.route('/')
def home():
    return render_template("index.html", post_list=data)


@app.route('/<post_id>')
def post(post_id):
    requested_post = data_dict[int(post_id)]
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    _load_data()
    app.run(debug=True)
