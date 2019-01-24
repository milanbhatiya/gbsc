from project.com.dao import *

class RegisterDAO:
    def insertRegister(self,registerVO):
        connection=conn_db()
        cursor1=connection.cursor()
        cursor1.execute('INSERT into registermaster(registerFirstname,registerLastname,registerEmailid,registerGender,registerAddress) VALUES("'+registerVO.registerFirstname+'","'+registerVO.registerLastname+'","'+registerVO.registerEmailid+'","'+registerVO.registerGender+'","'+registerVO.registerAddress+'")' )
        connection.commit()
        cursor1.close()
        connection.close()


