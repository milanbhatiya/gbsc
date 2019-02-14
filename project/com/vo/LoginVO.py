from wtforms import *

class LoginVO:
    loginId=IntegerField
    loginEmail=StringField
    loginPassword=StringField
    loginRole=StringField
    forgotPassword=StringField
    pwdDict=StringField