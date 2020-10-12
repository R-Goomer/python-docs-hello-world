from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')           ##links to the first page - upload.html
def index():
   return render_template("index.html")

@app.route('/output',methods=['POST'])
def process():                ##called when user input is given and submit button is pressed
    user_input = request.form["user_input"]
    return render_template("output.html",user_input=["Your Roll No is - E17CSE113"])


