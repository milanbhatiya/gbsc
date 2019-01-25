from project.com.dao import *

class LoginDAO:
    def insertLogin(self,loginVO):
        connection=conn_db()
        cursor1=connection.cursor()
        cursor1.execute('INSERT into loginmaster(loginEmailId) VALUES("'+loginVO.loginEmailId+'")' )

        connection.commit()
        cursor1.close()
        connection.close()

    def searchLoginId(self,loginVO):
        connection = conn_db()
        cursor1 = connection.cursor()
        cursor1.execute('select max(loginId) from loginmaster')
        loginDict=cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return loginDict