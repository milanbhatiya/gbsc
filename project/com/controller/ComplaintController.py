from project import app
from flask import Flask,render_template,request
from project.com.dao.ComplaintDAO import ComplaintDAO
from project.com.vo.ComplaintVO import ComplaintVO

@app.route('/viewComplaint')
def viewComplaint():
    return render_template('admin/viewComplaint.html')
@app.route('/addComplaints')
def addComplaint():
    return render_template('admin/addComplaint.html')