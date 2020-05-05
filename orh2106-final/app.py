# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: OliviaHartzell1


Olivia Hartzell
orh2106
final

"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__) #creates flask app variable

#static route
@app.route("/") #if go to website in there, and go to home route, will return whatever is defined in the following func
def hello():
    return render_template("index.html") # flask will look in templates directoryof current directory
    #return "Hello World!" #this is really html code here-
    #for external can just use href in the html file
    
    #go back to html file to link to site that i made:
    #change href and the reference
    #for the href-- "/columbia"


@app.route("/1006-work")
def my_site():
    return render_template("1006_stuff.html")
 #   return "<p> This is my new site! </p>"
 
 


@app.route("/other-work")
def new_site():
    return render_template("other_stuff.html")




#start the server
if __name__ == "__main__":
    app.run()
    
    #127.001 is same as localhost
    
    #git init 