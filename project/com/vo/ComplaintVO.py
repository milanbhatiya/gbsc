from wtforms import *

class ComplaintVO:
    complaintId=IntegerField
    complaintSubject=StringField
    complaintDescription=StringField
    complaintImageName= StringField
    complaintImagePath=StringField
    compalintDate=StringField
    complaintTime= StringField
    complaintStatus=StringField
    complaintActiveStatus=StringField
    complaintReply=StringField
    complaintTo_LoginId=StringField
    complaintFrom_LoginId=StringField