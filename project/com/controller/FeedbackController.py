from project import app
from flask import Flask,render_template,request,session,flash,redirect,url_for
from project.com.dao.FeedbackDAO import FeedbackDAO
from project.com.vo.FeedbackVO import FeedbackVO

@app.route('/viewFeedback')
def viewFeedback():
    try:
        if session['sessionloginDict']['loginRole'] == 'admin':
            return render_template('admin/viewFeedback.html')
        else:
            flash('you are not admin !, Please Login as Admin. ', 'danger')
            return redirect(url_for('loadLogin'))
    except:
        flash('Plese Login First !', 'danger')
        return redirect(url_for('loadLogin'))

@app.route('/addFeedback')
def addFeedback():
    try:
        if session['sessionloginDict']['loginRole'] == 'user':
            return render_template('admin/addFeedback.html')
        else:
            flash('Plese Login First !', 'danger')
            return redirect(url_for('loadLogin'))
    except:
        flash('Plese Login First !', 'danger')
        return redirect(url_for('loadLogin'))

@app.route('/insertFeedback')
def insertFeedback():
    try:
        if session['sessionloginDict']['loginRole'] == 'user':
            feedbackDAO = FeedbackDAO()
            feedbackVO = FeedbackVO()

            feedbackDescription = request.form['feedbackDescription']
            feedbackRating = request.form['feedbackRating']

            feedbackVO.feedbackDescription=feedbackDescription
            feedbackVO.feedbackRating=feedbackRating
            feedbackVO.feedbackActiveStatus='active'
            return render_template('admin/addFeedback.html')
        else:
            flash('Plese Login First !', 'danger')
            return redirect(url_for('loadLogin'))
    except:
        flash('Plese Login First !', 'danger')
        return redirect(url_for('loadLogin'))