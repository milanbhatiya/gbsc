from project import app
from flask import Flask,render_template,request,redirect,url_for
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO

@app.route('/checkLogin',methods=['post'])
def checkLogin():
    loginDAO=LoginDAO()
    loginVO=LoginVO()

    loginEmailId=request.form['loginEmailId']
    loginPassword=request.form['loginPassword']

    loginVO.loginEmailId=loginEmailId
    loginVO.loginPassword=loginPassword
    loginVO.loginRole='user'

    loginDict=loginDAO.searchLogin(loginVO)

    if len(loginDict)==0:
        return render_template('admin/login.html',loginerrorDict1='Invelid Email')
    elif loginDict[0]["loginPassword"]!=loginVO.loginPassword:
        return render_template('admin/login.html', loginerrorDict2='Invelid Password')
    elif loginDict[0]["loginRole"]=='admin':
        return redirect(url_for('adminHome'))
    elif loginDict[0]["loginRole"]=='user':
        return redirect(url_for('userHome'))