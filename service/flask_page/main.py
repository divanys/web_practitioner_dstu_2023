from flask import Flask


#Объект приложения
app = Flask(__name__)

@app.route("/")
def main_page():
    return "Main_page"



if __name__ == "__main__":
    app.run(debug=False)