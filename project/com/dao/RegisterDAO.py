from project.com.dao import *

class RegisterDAO:
    def insertRegister(self,registerVO):
        connection=conn_db()
        cursor1=connection.cursor()
        cursor1.execute('INSERT into registermaster(registerFirstname,registerLastname,registerGender,registerAddress,register_LoginId) VALUES("'+registerVO.registerFirstName+'","'+registerVO.registerLastName+'","'+registerVO.registerGender+'","'+registerVO.registerAddress+'","'+registerVO.register_LoginId+'")' )
        connection.commit()
        cursor1.close()
        connection.close()