from project.com.dao import *

class RegisterDAO:
    def insertRegister(self,registerVO):
        connection=conn_db()
        cursor1=connection.cursor()
        cursor1.execute('INSERT into registermaster(registerOrganizationname,registerMobileno,registerCategory,registerAddress,register_LoginId) VALUES("'+registerVO.registerOrganizationname+'","'+registerVO.registerMobileno+'","'+registerVO.registerCategory+'","'+registerVO.registerAddress+'","'+registerVO.register_LoginId+'")' )
        connection.commit()
        cursor1.close()
        connection.close()