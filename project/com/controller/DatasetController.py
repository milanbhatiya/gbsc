from project import app
from flask import Flask,render_template,request,redirect,url_for,session,flash
from project.com.dao.DatasetDAO import DatasetDAO
from project.com.vo.DatasetVO import DatasetVO
from werkzeug.utils import secure_filename
import os


@app.route('/loadDataset')
def loadDataset():
    try:
        if session['sessionloginDict']['loginRole'] == 'admin':
            return render_template('admin/addDataset.html')
        else:
            flash('you are not admin !, Please Login as Admin. ', 'danger')
            return redirect(url_for('loadLogin'))
    except:
        flash('Plese Login First !', 'danger')
        return redirect(url_for('loadLogin'))


@app.route('/insertDataset',methods=['POST'])
def insertDataset():
    try:
        if session['sessionloginDict']['loginRole'] == 'admin':
            datasetDAO=DatasetDAO()
            datasetVO=DatasetVO()

            UPLOAD_FOLDER = r'C:\Users\User\PycharmProjects\gbsc\project\static\dataset'
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

            print("kreykfjsdkmlerksd.j,m")
            file = request.files['datasetFile']


            print(file)
            datasetVO.datasetName = secure_filename(file.filename)

            datasetVO.datasetPath = os.path.join(app.config['UPLOAD_FOLDER'])

            file.save(os.path.join(app.config['UPLOAD_FOLDER'],datasetVO.datasetName))
            datasetVO.datasetDescription = request.form['datasetDescription']
            datasetVO.datasetActiveStatus='active'
            datasetDAO.insertDataset(datasetVO)

            return  render_template("admin/addDataset.html")
        else:
            flash('you are not admin !, Please Login as Admin. ', 'danger')
            return redirect(url_for('loadLogin'))
    except:
        flash('Plese Login First !', 'danger')
        return redirect(url_for('loadLogin'))


@app.route('/viewDataset')
def viewDataset():
    try:
        if session['sessionloginDict']['loginRole'] == 'admin':
            datasetDAO=DatasetDAO()
            datasetVO=DatasetVO()
            datasetDict=datasetDAO.viewDataset(datasetVO)
            return render_template('admin/viewDataset.html',datasetDict=datasetDict)
        else:
            flash('you are not admin !, Please Login as Admin. ', 'danger')
            return redirect(url_for('loadLogin'))
    except:
        flash('Plese Login First !', 'danger')
        return redirect(url_for('loadLogin'))


@app.route('/deleteDataset',methods=['get'])
def deleteDataset():
    try:
        if session['sessionloginDict']['loginRole'] == 'admin':
            datasetDAO=DatasetDAO()
            datasetVO=DatasetVO()
            datasetVO.datasetId=request.args.get('datasetId')
            datasetVO.datasetActiveStatus="deactive"
            datasetDAO.deleteDataset(datasetVO)
            return redirect(url_for("viewDataset"))
        else:
            flash('you are not admin !, Please Login as Admin. ', 'danger')
            return redirect(url_for('loadLogin'))
    except:
        flash('Plese Login First !', 'danger')
        return redirect(url_for('loadLogin'))