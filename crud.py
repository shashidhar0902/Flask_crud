from flask import Flask, redirect, render_template, request

app = Flask(__name__)

#index routing to render template index.html 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')
#/login
@app.route('/logincheck', methods= ['POST','GET'])
def login_check():
    #if request method is post validate login credentials
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return redirect('/crudprop')
    else:
        return render_template('login.html')

#/homepage
@app.route('/crudprop')
def homepage():
    return render_template('crudprop.html')

prop_list = []
@app.route('/addproperty', methods= ['POST','GET'])
def addprop():
    if request.method == 'POST':
        prop = request.form['name']
        prop_list.append(prop)
        print(prop_list)
        return redirect('/crudprop')
    else:
        return render_template('crudprop.html')

#/deleteprop
@app.route('/deleteproperty', methods = ['POST'])
def deleteprop():
    if request.method == 'POST':
        prop = request.form['name']
    if prop in prop_list:
        prop_list.remove(prop)
    print(prop_list)
    return redirect('/crudprop')

# run app
if __name__ == '__main__':
    app.run(debug=True)