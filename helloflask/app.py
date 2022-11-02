from unicodedata import name
from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
@app.route("/hello/<name>")
@app.route("/square/")
@app.route("/square/<int:num>")
def hello(name=None):
    if name:
        return render_template("hello.html",username=name)
    else:
        return render_template("hello.html",username="World")

def square(num=None):
    if num:
        result= int(num) ** 2
        return str(result)
    else: 
        return 'you need to provide a number in URL after/sqaure/'

if __name__=='__main__':
    app.run(debug=True) 
    