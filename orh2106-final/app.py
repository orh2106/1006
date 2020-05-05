# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: OliviaHartzell1


Olivia Hartzell
orh2106
final


Below I use flask to create a site that uses html files in the templates folder
and the images and objects in the static folder.
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__) #creates flask app variable

#static route
@app.route("/") 
def hello():
    return render_template("index.html") 



@app.route("/1006-work")
def my_site():
    return render_template("1006_stuff.html")

 


@app.route("/other-work")
def new_site():
    return render_template("other_stuff.html")




#start the server
if __name__ == "__main__":
    app.run()
    
    
    