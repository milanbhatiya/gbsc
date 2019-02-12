from wtforms import *

class FeedbackVO:
    feedbackId=IntegerField
    feedbackDescription=StringField
    feedbackRating=StringField
    feedbackDate=StringField
    feedbackTime=StringField
    feedbackActiveStatus=StringField
    feedbackFrom_LoginId=StringField
    feedbackTo_LoginId=StringField