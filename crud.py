from flask import Flask, jsonify, make_response, redirect, render_template, request, session, url_for
from datetime import timedelta
import secrets

app = Flask(__name__)

app.secret_key = secrets.token_hex()
app.permanent_session_lifetime = timedelta(seconds=5)

#index routing to render template index.html 
@app.route('/')
def index():
    return render_template('index.html')

#index routing to render template login.html 
@app.route('/loginpage')
def loginpage():
    return render_template('login.html')

#/login
@app.route('/login', methods= ['POST','GET'])
def login():
    #if request method is post validate login credentials
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        if user == 'admin' and password == 'admin':
            session["admin"] = user
            session.permanent = True
            # resp = make_response(redirect('/crudprop'))
            # resp.set_cookie('user',user)
            # return resp
            return redirect(url_for("homepage"))
    else:
        if "admin" in session:
            return redirect(url_for("homepage"))
        return redirect(url_for('loginpage'))

""" upload the file here in this route and saving
 it and redirecting to a page that th
file is uploaded successfully"""
@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
      f = request.files['file'] 
      f.save(f.filename)
      return 'file uploaded successfully'

#logout
@app.route('/logout')
def logout():
    session.pop("admin", None)
    return redirect(url_for('index'))

#/homepage
@app.route('/crudprop')
def homepage():
    if "admin" in session:
        return render_template('crudprop.html')
    else:
        return redirect(url_for('index'))    

prop_list = []
@app.route('/addproperty', methods= ['POST','GET'])
def addprop():
    if request.method == 'POST':
        prop_id = request.form['id']
        prop_address = request.form['address']
        data = {
            'id': prop_id,
            'address': prop_address
        }
        prop_list.append(data)
        print(prop_list)
        return redirect('/crudprop')
    else:
        return render_template('crudprop.html')

#/deleteprop
@app.route('/deleteproperty', methods = ['POST'])
def deleteprop():
    if request.method == 'POST':
        prop_id = request.form['id']
    for item in prop_list:
        if item['id'] == prop_id:
            prop_list.remove(item)
    print(prop_list)
    return redirect('/crudprop')

# run app
if __name__ == '__main__':
    app.run(debug=True)