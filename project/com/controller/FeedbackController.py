from project import app
from flask import Flask,render_template,request
from project.com.dao.FeedbackDAO import FeedbackDAO
from project.com.vo.FeedbackVO import FeedbackVO

@app.route('/viewFeedback')
def viewFeedback():
    return render_template('admin/viewFeedback.html')

@app.route('/addFeedback')
def addFeedback():
    return render_template('admin/addFeedback.html')

@app.route('/insertFeedback')
def insertFeedback():
    feedbackDAO = FeedbackDAO()
    feedbackVO = FeedbackVO()

    feedbackDescription = request.form['feedbackDescription']
    feedbackRating = request.form['feedbackRating']

    feedbackVO.feedbackText=feedbackDescription
    feedbackVO.feedbackRating=feedbackRating
    feedbackVO.feedbackActiveStatus='active'
    return render_template('admin/addFeedback.html')