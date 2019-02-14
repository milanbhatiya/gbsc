from project import app
from flask import Flask,render_template,request,session,redirect,flash,url_for
from project.com.dao.ComplaintDAO import ComplaintDAO
from project.com.vo.ComplaintVO import ComplaintVO

@app.route('/viewComplaint')
def viewComplaint():
    try:
        if session['sessionloginDict']['loginRole'] == 'admin':
            return render_template('admin/viewComplaint.html')
        else:
            flash('you are not admin !, Please Login as Admin. ', 'danger')
            return redirect(url_for('loadLogin'))
    except:
        flash('Plese Login First !', 'danger')
        return redirect(url_for('loadLogin'))
@app.route('/addComplaint')
def addComplaint():
    try:
        if session['sessionloginDict']['loginRole'] == 'user':
            return render_template('admin/addComplaint.html')
        else:
            flash('Plese Login First !', 'danger')
            return redirect(url_for('loadLogin'))
    except:
        flash('Plese Login First !', 'danger')
        return redirect(url_for('loadLogin'))
