from project import app
from flask import Flask,render_template,request
from project.com.dao.RegisterDAO import RegisterDAO
from project.com.vo.RegisterVO import RegisterVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO
import random
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

@app.route('/register')
def loadRegister():
    return render_template('admin/register.html')

@app.route('/resetpassword')
def resetPassword():
    return render_template('admin/resetpassword.html')


@app.route('/insertRegister', methods=['POST'])
def insertRegister():
    registerDAO=RegisterDAO()
    registerVO=RegisterVO()
    loginDAO=LoginDAO()
    loginVO=LoginVO()

    registerPassword = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))

    registerFirstname=request.form['registerFirstname']
    registerLastname=request.form['registerLastname']
    registerGender=request.form['registerGender']
    registerAddress=request.form['registerAddress']
    loginEmailId = request.form['registerEmailid']


    registerVO.registerFirstName=registerFirstname
    registerVO.registerLastName=registerLastname
    registerVO.registerGender=registerGender
    registerVO.registerAddress=registerAddress
    loginVO.loginEmailId=loginEmailId
    loginVO.loginPassword=registerPassword
    loginVO.loginRole='user'

    loginDAO.insertLogin(loginVO)

    registerVO.register_LoginId=str(loginDAO.searchLoginId(loginVO)[0].values()[0])
    registerDAO.insertRegister(registerVO)

    print("registerPassword=" + registerPassword)

    fromaddr = "gesturebasedsmartcommunicator@gmail.com"

    toaddr = loginVO.loginEmailId

    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = "PYTHON PASSWORD"

    msg.attach(MIMEText(registerPassword, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(fromaddr, "BHAIbhai4725")

    text = msg.as_string()

    server.sendmail(fromaddr, toaddr, text)

    server.quit()

    return render_template('admin/login.html')