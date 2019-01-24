from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('admin/sign-up.html')

@app.route('/viewcomplain')
def managecomplain():
    return render_template('admin/managecomplain.html')