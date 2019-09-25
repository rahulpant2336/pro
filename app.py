import os
from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.config['SECRET_KEY'] = '331512'

#recaptcha


############################################
########### SQL DATABASE SECTION ###########
###########################################


#__file__ --> c:/users/rahul/desktop/myflask/app.py


############################################
######### MODELS ##########################
##########################################



###########################################
#### VIEW FUNCTIONS -- HAVE FORMS #########
##########################################

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
   app.run(debug = True)
