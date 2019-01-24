from wtforms import *

class RegisterVO:
    registerId=IntegerField
    registerFirstname=StringField
    registerLastname=StringField
    registerEmailid=StringField
    registerAddress=StringField
    registerGender=StringField