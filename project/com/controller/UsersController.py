from project import app
from flask import Flask,render_template,request,url_for

@app.route('/viewUsers')
def viewUsers():
    return render_template('admin/viewUsers.html')