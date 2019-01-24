from project import app
from flask import Flask,render_template,request
from project.com.dao.RegisterDAO import RegisterDAO
from project.com.vo.RegisterVO import RegisterVO


@app.route('/')
def default():
    return render_template('admin/Register.html')


@app.route('/register', methods=['POST'])
def register():
    registerDAO=RegisterDAO()
    registerVO=RegisterVO()

    registerFirstname=request.form['RegisterFirstname']
    registerLastname=request.form['RegisterLastname']
    registerEmailid=request.form['RegisterEmailid']
    registerGender=request.form['RegisterGender']
    registerAddress=request.form['RegisterAddress']

    registerVO.registerFirstname=registerFirstname
    registerVO.registerLastname=registerLastname
    registerVO.registerEmailid=registerEmailid
    registerVO.registerGender=registerGender
    registerVO.registerAddress=registerAddress

    registerDAO.insertRegister(registerVO)

    return render_template('admin/welcome.html')
