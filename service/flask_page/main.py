from flask import Flask, render_template


#Объект приложения
app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/articles")
def article_page():
    return render_template("article.html")

@app.route("/create_article")
def create_article_page():
    return render_template("create_article.html")

@app.route("/article_show")
def article_show():
    return render_template("article_show")



if __name__ == "__main__":
    app.run(debug=False)