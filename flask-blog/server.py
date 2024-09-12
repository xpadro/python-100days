from flask import Flask, render_template

app = Flask(__name__)


@app.route("/blog")
def home():
    articles = ['article a', 'article b', 'article c']
    return render_template("blog.html", author='Xavi', article_list=articles)


if __name__ == '__main__':
    # Debug mode enables hot reloading and debugging
    app.run(debug=True)
