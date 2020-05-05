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
    #return "<b> Test 123 </b>"
    #we can take advanage of render template
    return render_template("index.html") # flask will look in templates directoryof current directory
    #return "Hello World!" #this is really html code here-
    #for external can just use href in the html file
    
    #go back to html file to link to site that i made:
    #change href and the reference
    #for the href-- "/columbia"


#@app.route("/1006")
#def my_site():
 #   return "<p> This is my new site! </p>"


#make a file that has alink from one page to another page
    #use href attribute


#@app.route("/columbia")
#def my_fun():

#start the server
if __name__ == "__main__":
    app.run()
    
    #127.001 is same as localhost
    
    #git init 