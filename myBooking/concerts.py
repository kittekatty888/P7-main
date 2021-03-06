#Flask code#
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Frontpage(): #Define pop site#
    return render_template("Parent.html") #Return #

@app.route("/pop") # Here we define which subpage the following code relates to
def pop(): #Define pop site#
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect database to HTML
    rows = db_cursor.execute("SELECT * FROM concerts where genre='Pop'") #Find the concerts matching the criteria, e.g. genre, date, etc.
    return render_template("P7.html", rows=rows, Overskrift="Pop concerts") #Return pop - her skal jeg undersøge hvordan man gør overskriften dynamisk 

@app.route("/jazz")
def Jazz(): #Define pop site#
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect database to HTML
    rows = db_cursor.execute("SELECT * FROM concerts where genre='Jazz'") #Execute the concerts database
    return render_template("P7.html", rows=rows) #Return #

@app.route("/classic")
def Klassisk(): #Define pop site#
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect database to HTML
    rows = db_cursor.execute("SELECT * FROM concerts where genre='Klassisk'") #Execute the concerts database
    return render_template("P7.html", rows=rows) #Return #

@app.route("/rock")
def Rock(): #Define pop site#
    db = sqlite3.connect("concerts.db", isolation_level=None) #Connect database to HTML
    db_cursor = db.cursor() #Connect database to HTML
    rows = db_cursor.execute("SELECT * FROM concerts where genre='Rock'") #Execute the concerts database
    return render_template("P7.html", rows=rows) #Return #
