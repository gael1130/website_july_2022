from flask import Flask, url_for, request, render_template, redirect
from markupsafe import escape

# https://flask.palletsprojects.com/en/2.1.x/quickstart/#url-building


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

#
# @app.route("/username/<name>/<int:number>")
# def greet(name, number):
#     return f"Hello {name}, your are {number} years old"


#
# @app.route("/")
# def index():
#     return redirect(url_for("Index Page"))
#     # return "Index Page"


# @app.route("/hello")
# def hello_world():
#     return render_template("hello.html")
#     # return redirect(url_for("hello"))
#     # return "Hello World!"



#
# @app.route("/strata")
# def strata():
#     return render_template("index.html")


# *** Variable Rules ***


# @app.route("/user/<username>")
# def show_user_profile(username):
#     #     show the user profile for that user
#     return "User %s" % escape(username)
#
#
# @app.route("/post/<int:post_id>")
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return "Post %d" % post_id


# @app.route("/path:<path:subpath>")
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return "Subpath %s" % escape(subpath)


# *** Unique URLs / Redirection Behavior ***

#
# @app.route("/projects/")
# def projects():
#     return "The project page"
#
#
# @app.route("/about")
# def about():
#     return "The about page"


# URL Building


# @app.route("/login")
# def login():
#     return "login"
#
#
# @app.route("/user/<username>")
# def profile(username):
#     return f"{username}\'s profile"


#
# with app.test_request_context():
#     print(url_for("index"))
#     print(url_for("login"))
#     print(url_for("login", next="/"))
#     print(url_for("profile", username="John Doe"))


# @app.route("/login", methods=["Get", "POST"])
# def login():
#     if request.method == "POST":
#         return do_the_login()
#     else:
#         return show_the_login_form()


# *** STATIC FILES ***


# *** RENDERING TEMPLATES ***
#
# @app.route("/hello/<name>")
# def hello(name=None):
#     return render_template("hello.html", name=name)


# *** Redirect ***

# ****


if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
