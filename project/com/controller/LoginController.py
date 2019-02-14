from project import app
from flask import render_template, request, redirect, url_for, session, flash
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO


@app.route('/')
@app.route('/loadLogin')
def loadLogin():
    return render_template('admin/login.html')


@app.route('/checkLogin', methods=['post'])
def checkLogin():
    loginDAO = LoginDAO()
    loginVO = LoginVO()

    loginEmail = request.form['loginEmail']
    loginPassword = request.form['loginPassword']

    loginVO.loginEmail = loginEmail
    loginVO.loginPassword = loginPassword

    loginDict = loginDAO.searchLogin(loginVO)
    print(loginDict)
    if len(loginDict) == 0:
        flash('Invalid Email !', 'danger')
        return redirect(url_for('loadLogin'))
    elif loginDict[0]["loginPassword"] != loginVO.loginPassword:
        flash('Invalid Password !', 'danger')
        return redirect(url_for('loadLogin'))
    elif loginDict[0]["loginRole"] == 'admin':
        session['sessionloginDict'] = loginDict[0]
        # flash('Login Success for Admin', 'success')
        return redirect(url_for('adminHome'))
    elif loginDict[0]["loginRole"] == 'user':
        session['sessionloginDict'] = loginDict[0]
        # flash('Login Success for User', 'success')
        return redirect(url_for('userHome'))


@app.route('/logout')
def logout():
    session.clear()
    flash('Logout Success.', 'success')
    return redirect(url_for('loadLogin'))


@app.route('/adminHome')
def adminHome():
    try:
        if session['sessionloginDict']['loginRole'] == 'admin':
            return render_template('admin/index.html')
        else:
            flash('Plese Login First ! ', 'danger')
            return redirect(url_for('loadLogin'))
    except:
        flash('Plese Login First !', 'danger')
        return redirect(url_for('loadLogin'))

@app.route('/userHome')
def userHome():
    try:
        if session['sessionloginDict']['loginRole'] == 'admin':
            return render_template('admin/welcome.html')
        else:
            flash('Plese Login First ! ', 'danger')
            return redirect(url_for('loadLogin'))
    except:
        flash('Plese Login First !', 'danger')
        return redirect(url_for('loadLogin'))