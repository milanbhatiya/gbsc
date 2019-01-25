from wtforms import *

class RegisterVO:
    registerId=IntegerField
    registerFirstName=StringField
    registerLastName=StringField
    registerAddress=StringField
    registerGender=StringField
    register_LoginId=StringField