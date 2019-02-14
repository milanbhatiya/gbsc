from project import app
from flask import Flask,render_template,request,redirect,url_for,flash
from project.com.dao.RegisterDAO import RegisterDAO
from project.com.vo.RegisterVO import RegisterVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO
import random
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


@app.route('/loadRegister')
def loadRegister():
    return render_template('admin/register.html')


@app.route('/insertRegister', methods=['POST'])
def insertRegister():
    registerDAO=RegisterDAO()
    registerVO=RegisterVO()
    loginDAO=LoginDAO()
    loginVO=LoginVO()
    registerVO.registerOrganizationname=request.form['registerOrganizatonname']
    registerVO.registerContact=request.form['registerContact']
    registerVO.registerCategory=request.form['registerCategory']
    registerVO.registerAddress=request.form['registerAddress']
    registerVO.register_LoginId = str(loginDAO.searchLoginId(loginVO)[0].values()[0])
    loginVO.loginEmail = request.form['registerEmail']
    loginVO.loginPassword = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))
    loginVO.loginRole='user'
    print(loginVO.loginEmail)
    loginDict = loginDAO.searchLogin(loginVO)
    if len(loginDict) == 0:
        print("registerPassword=" + loginVO.loginPassword)
        fromaddr = "gesturebasedsmartcommunicator@gmail.com"
        toaddr = loginVO.loginEmail
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "PYTHON PASSWORD"
        msg.attach(MIMEText(loginVO.loginPassword, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "BHAIbhai4725")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        loginDAO.insertLogin(loginVO)

        registerDAO.insertRegister(registerVO)
        return redirect(url_for('loadLogin'))
    else:
        flash('Email already exist !', 'danger')
        return redirect(url_for('loadRegister'))


@app.route('/forgotPassword')
def forgotPassword():
    return render_template('admin/forgotPassword.html')

@app.route('/resetPassword', methods=['post'])
def resetPPassword():
    loginDAO = LoginDAO()
    loginVO = LoginVO()
    forgotPassword = request.form['forgotPassword']
    loginVO.forgotPassword = forgotPassword
    searchPasswordDict = loginDAO.searchForgotPassword(loginVO)
    # if len(searchPasswordDict)==0:
    #     flash('Invalid Email !','danger')
    #     return redirect(url_for('forgotPassword'))
    # else:
    loginVO.loginPassword = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))
    print(loginVO.pwdDict)
    print(searchPasswordDict)
    print("registerPassword=" + loginVO.loginPassword)
    fromaddr = "gesturebasedsmartcommunicator@gmail.com"
    toaddr = loginVO.forgotPassword
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "PYTHON PASSWORD"
    msg.attach(MIMEText(loginVO.loginPassword, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "BHAIbhai4725")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
    except:
        return
    loginDAO.resetPassword(loginVO)
    flash('Password Sent,Check Your Email','success')
    return redirect(url_for('loadLogin'))
    # return render_template('admin/forgotPassword.html')