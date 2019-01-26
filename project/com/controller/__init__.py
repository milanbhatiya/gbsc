from project import app
from flask import Flask,render_template
import project.com.controller.RegisterController


@app.route('/')
def loadIndex():
    return render_template('admin/index.html')