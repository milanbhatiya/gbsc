from project import app
from flask import Flask,render_template
import project.com.controller.RegisterController
import project.com.controller.UsersController


@app.route('/')
def loadLogin():
    return render_template('admin/viewUsers.html')