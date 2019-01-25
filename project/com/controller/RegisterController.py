from project import app
from flask import Flask,render_template,request
from project.com.dao.RegisterDAO import RegisterDAO
from project.com.vo.RegisterVO import RegisterVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO

@app.route('/')
def loadIndex():
    return render_template('admin/index.html')
@app.route('/register')
def register():
    return render_template('admin/register.html')

@app.route('/login')
def login():
    return render_template('admin/sign-in.html')

# @app.route('/register')
# def register():
#     return render_template('admin/register.html')

@app.route('/insertRegister', methods=['POST'])
def insertRegister():
    registerDAO=RegisterDAO()
    registerVO=RegisterVO()
    loginDAO=LoginDAO()
    loginVO=LoginVO()


    registerFirstname=request.form['registerFirstname']
    registerLastname=request.form['registerLastname']
    registerGender=request.form['registerGender']
    registerAddress=request.form['registerAddress']
    loginEmailId = request.form['registerEmailid']


    registerVO.registerFirstName=registerFirstname
    registerVO.registerLastName=registerLastname
    registerVO.registerGender=registerGender
    registerVO.registerAddress=registerAddress
    print registerVO.registerAddress, registerVO.registerFirstName, registerVO.registerGender, registerVO.registerLastName
    loginVO.loginEmailId=loginEmailId

    loginDAO.insertLogin(loginVO)

    registerVO.register_LoginId=str(loginDAO.searchLoginId(loginVO)[0].values()[0])
    print registerVO.register_LoginId
    registerDAO.insertRegister(registerVO)



    return render_template('admin/welcome.html')
