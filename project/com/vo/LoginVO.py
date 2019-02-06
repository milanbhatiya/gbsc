from wtforms import *

class LoginVO:
    loginId=IntegerField
    loginEmailId=StringField
    loginPassword=StringField
    loginRole=StringField