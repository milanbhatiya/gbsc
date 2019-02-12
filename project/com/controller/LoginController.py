from project import app
from flask import render_template,request,redirect,url_for,session
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO


@app.route('/')
def loadLogin():

    return render_template('admin/login.html')


@app.route('/checkLogin',methods=['post'])
def checkLogin():
    loginDAO=LoginDAO()
    loginVO=LoginVO()

    loginEmail=request.form['loginEmail']
    loginPassword=request.form['loginPassword']

    loginVO.loginEmail=loginEmail
    loginVO.loginPassword=loginPassword

    loginDict=loginDAO.searchLogin(loginVO)

    if len(loginDict)==0:
        return render_template('admin/login.html',loginerrorDict1='Invalid Email')
    elif loginDict[0]["loginPassword"]!=loginVO.loginPassword:
        return render_template('admin/login.html', loginerrorDict2='Invalid Password')
    elif loginDict[0]["loginRole"]=='admin':
        session['sessionloginDict']=loginDict[0]
        return redirect(url_for('adminHome'))
    elif loginDict[0]["loginRole"]=='user':
        session['sessionloginDict'] = loginDict[0]
        return redirect(url_for('userHome'))

@app.route('/logout')
def logout():
    session.clear()

    return render_template('admin/login.html', Logout='Logout Successfully')
