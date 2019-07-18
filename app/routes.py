from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/index1.html')
def newroute():
    return render_template("index1.html")

@app.route('/index2.html')
def newerroute():
    return render_template("index2.html")
    
@app.route('/index3.html')
def newishroute():
    return render_template("index3.html")
    
@app.route('/index4.html')
def newerishroute():
    return render_template("index4.html")
    
@app.route('/index5.html')
def notnewroute():
    return render_template("index5.html")