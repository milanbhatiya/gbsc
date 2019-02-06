from wtforms import *

class FeedbackVO:
    feedbackId=IntegerField
    feedbackText=StringField
    feedbackRating=StringField
    feedbackDate=StringField
    feedbackTime=StringField
    feedback_LoginId=StringField