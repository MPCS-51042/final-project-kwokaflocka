from flask import Flask, render_template, url_for
app = Flask(__name__)

recipes = [
    {
        "author": "Sally",
        "recipe_name": "chicken alfredo",
        "ingredient": "chicken",
        "calories": "120"
    },
    {
        "author": "Alan",
        "recipe_name": "noodles",
        "ingredient": "soup",
        "calories": "300"
    }
]

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html', recipes=recipes)

@app.route("/about")
def about_page():
    return "<p>About this site</p>"


if __name__ == '__main__':
    app.run(debug=True)