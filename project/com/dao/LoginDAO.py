from project.com.dao import *

class LoginDAO:
    def insertLogin(self,loginVO):
        connection=conn_db()
        cursor1=connection.cursor()
        cursor1.execute('INSERT into loginmaster(loginEmail,loginPassword,loginRole) VALUES("'+loginVO.loginEmail+'","'+loginVO.loginPassword+'","'+loginVO.loginRole+'")' )

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
        cursor1.execute("select * from loginmaster where loginEmail=('"+loginVO.loginEmail+"')")
        loginDict=cursor1.fetchall()
        cursor1.close()
        connection.close()
        return loginDict

    def searchForgotPassword(self,loginVO):
        connection=conn_db()
        cursor1=connection.cursor()
        cursor1.execute("select * from loginmaster where loginEmail=('"+loginVO.forgotPassword+"')")
        searchPasswordDict=cursor1.fetchall()
        cursor1.close()
        connection.close()
        return searchPasswordDict

    # def forgotPassword(self,loginVO):
    #     connection=conn_db()
    #     cursor1=connection.cursor()
    #     cursor1.execute("select * from loginmaster where loginPassword=('"+loginVO.loginPassword+"')")
    #     pwdDict=cursor1.fetchall()
    #     cursor1.close()
    #     connection.close()
    #     print(pwdDict)
    #     return pwdDict

    def resetPassword(self,loginVO):
        connection=conn_db()
        cursor1=connection.cursor()
        cursor1.execute('UPDATE loginmaster SET loginPassword ="'+loginVO.loginPassword+'"WHERE loginEmail="'+loginVO.forgotPassword+'"' )
        connection.commit()
        cursor1.close()
        connection.close()