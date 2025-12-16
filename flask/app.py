# Importing flask module into the app python file
from flask import Flask, request

# create an instance of the flask class
# The name of the module will be called (__name__)is passed
# to help Flask determine the root path of the application
app = Flask(__name__)

#====================================================================#
# Routes go here...

# Define a route for the default root URL
# the app.route() function will map out the URL to a specific function
# in this case the "home()" function
@app.route("/")
def home():
    return "Hello, class"

# new route for about page
@app.route("/aboutUs")
def aboutUs():
    return "Welcome to the about page.. This is currently under contruction.."

# new route for contact page
@app.route("/contact")
def contact():
    return "Welcome to the contact page.. This is currently under contruction.."

# This is a dynamic URL, where the value enter in place of
# <username> is used in the python function
# where it is added to the out string
@app.route("/user/<username>")
def userPage(username):
    return f"Welcome to your profile '{username}'..."


@app.route("/item/<int:itemId>")
def getItem(itemId):
    return f"Item ID: '{itemId}'..."

# square root
@app.route("/square/<int:number>")
def getNumber(number):
    square = number * number 
    return f"this is it '{square}'"

@app.route("/methodTest")
def methodTest():
    if request.method == "GET":
        return "You used GET!"
    
    elif request.method == "POST":
        return "You used POST!"
    
    else:
        return TypeError

#====================================================================#

# the content below must remain at the bottom of the python file
# check if the script is being run directly (not imported as a module)
if __name__ == "__main__": 
    # run the last application
    # sets the debug to true so  the debug mode
    # will auto reload and provide error messages
    app.run(port=8080, debug=True)
