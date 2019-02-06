from project.com.dao import *

class LoginDAO:
    def insertLogin(self,loginVO):
        connection=conn_db()
        cursor1=connection.cursor()
        cursor1.execute('INSERT into loginmaster(loginEmailId,loginPassword,loginRole) VALUES("'+loginVO.loginEmailId+'","'+loginVO.loginPassword+'","'+loginVO.loginRole+'")' )

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

    def searchLogin(self,loginVO):
        connection=conn_db()
        cursor1=connection.cursor()
        cursor1.execute("select * from loginmaster where loginEmailId='"+loginVO.loginEmailId+"'")
        loginDict=cursor1.fetchall()
        cursor1.close()
        connection.close()
        return loginDict
