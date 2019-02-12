from project import app
from flask import render_template
import project.com.controller.RegisterController
import project.com.controller.UserController
import project.com.controller.ComplaintController
import project.com.controller.DatasetController
import project.com.controller.FeedbackController
import project.com.controller.LoginController


@app.route('/adminHome')
def adminHome():
    return render_template('admin/index.html')

@app.route('/userHome')
def userHome():
    return render_template('admin/welcome.html')