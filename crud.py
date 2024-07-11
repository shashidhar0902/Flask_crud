from flask import Flask, jsonify, make_response, redirect, render_template, request, session, url_for

app = Flask(__name__)

app.secret_key = "hellosecret"

#index routing to render template index.html 
@app.route('/')
def index():
    return render_template('index.html')

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
            # resp = make_response(redirect('/crudprop'))
            # resp.set_cookie('user',user)
            # return resp
            return redirect(url_for("homepage"))
    else:
        if "admin" in session:
            return redirect(url_for("homepage"))
        return redirect(url_for('loginpage'))

#logout
@app.route('/logout')
def logout():
    session.pop("admin", None)
    return redirect(url_for('index'))

#/homepage
@app.route('/crudprop')
def homepage():
    return render_template('crudprop.html')

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