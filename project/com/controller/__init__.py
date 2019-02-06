from project import app
from flask import Flask,render_template,redirect,url_for
import project.com.controller.RegisterController
import project.com.controller.UsersController
import project.com.controller.ComplaintController
import project.com.controller.DatasetController
import project.com.controller.FeedbackController
import project.com.controller.LoginController

@app.route('/')
def loadLogin():
    return render_template('admin/login.html')

@app.route('/adminHome')
def adminHome():
    return render_template('admin/index.html')

@app.route('/userHome')
def userHome():
    return render_template('admin/welcome.html')