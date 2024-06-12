from flask import Flask, render_template

app = Flask(__name__)

posts=[]

@app.route("/")
@app.route("/home")
def homepage():
    return render_template('home.html')

@app.route("/login")
def homepage():
    return render_template('login.html')

if  __name__ == "__main__":
    app.run(debug=True)