from project import app
from flask import Flask,render_template
import project.com.controller.RegisterController
import project.com.controller.UsersController
import project.com.controller.ComplaintController
import project.com.controller.DatasetController
import project.com.controller.FeedbackController


@app.route('/')
def loadLogin():
    return render_template('admin/index.html')