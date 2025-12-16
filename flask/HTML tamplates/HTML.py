from flask import Flask, request, render_template

app = Flask(__name__)

#============================================#


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/form", methods = ["POST"])
def handle_form():
    user_name = request.form.get("user_name")
    Password = request.form.get("Password")
    return render_template("output.html", Password = Password,user_name = user_name )












#============================================#
if __name__ == "__main__":
    app.run(port= 8080, debug = True)