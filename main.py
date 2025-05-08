from flask import Flask, render_template, redirect, request,url_for, flash, session

from database import check_user, add_user

from flask_bcrypt import Bcrypt

app=Flask(__name__)
app.secret_key = 'kkju'

bcrypt=Bcrypt(app)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        phone_number=request.form['pnum']
        password=request.form['pass']

        hashed_password=bcrypt.generate_password_hash(password).decode('utf-8')
        user=check_user(email)

        if not user:
            new_user=(name,email,phone_number,hashed_password)
            add_user(new_user)
            flash('Registration successful. You can now log in.', 'success')
            return redirect(url_for('login'))
        else:
            # print('already registered')
            flash('User already registered. Please login.', 'warning')
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['pass']

        user=check_user(email)
        if not user:
            flash('User not available, please register', 'danger')
            return redirect(url_for('register'))
        else:
            if bcrypt.check_password_hash(user[-1],password):
                flash('Logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Password mismatch', 'danger')
                # print('wrong password')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

app.run(debug=True)