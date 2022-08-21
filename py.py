import csv
from urllib import request
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)     # created an instance of class flask
# __name__  is the main file which is the name of our app

@app.route("/")           # created a route to let others connect to our server(main route or localhost)  
def my_home():
    return render_template('index.html')

@app.route("/doc")        # can create any route  
def docs():
    return "<p>These are my documents</p>"

@app.route("/doc/happy")             
def happy():
    return "<p>*** HAPPY ME :) ***</p>"

@app.route("/render")           
def render():
    return render_template('myindex.html')
    
@app.route("/<username>/<int:post_id>")           
def name(username=None, post_id=None):
    return render_template('name.html', name=username, post_id=post_id)

@app.route("/<string:page_name>")             
def html_name(page_name):
    return render_template(page_name)
'''
def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.csv','a') as f :
        csv_writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
'''
@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST': 
        data = (request.form.to_dict())
        email = data['email']
        subject = data['subject']
        message = data['message']
        with open('database.csv','a') as f:
            csv_writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email,subject,message])
        return redirect('/thanku.html')
    else:
        return 'Oopss try again later :('
