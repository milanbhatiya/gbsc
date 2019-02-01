from project import app
from flask import Flask,render_template,request
from project.com.dao.DatasetDAO import DatasetDAO
from project.com.vo.DatasetVO import DatasetVO

@app.route('/viewDataset')
def viewDataset():
    return render_template('admin/viewDataset.html')

@app.route('/addDataset')
def addDataset():
    return render_template('admin/addDataset.html')