from wtforms import *

class RegisterVO:
    registerId=IntegerField
    registerOrganizationname=StringField
    registerContact=StringField
    registerAddress=StringField
    registerCategory=StringField
    register_LoginId=StringField