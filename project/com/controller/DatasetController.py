from project import app
from flask import Flask,render_template,request,redirect,url_for
from project.com.dao.DatasetDAO import DatasetDAO
from project.com.vo.DatasetVO import DatasetVO
from werkzeug.utils import secure_filename
import os

@app.route('/addDataset')
def Dataset():
    return render_template('admin/addDataset.html')

@app.route('/insertDataset',methods=['POST'])
def insertDataset():

    datasetDAO=DatasetDAO()
    datasetVO=DatasetVO()

    UPLOAD_FOLDER = r'C:\Users\User\PycharmProjects\gbsc\project\static\dataset'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    file = request.files['datasetFile']

    datasetVO.datasetName = secure_filename(file.filename)

    datasetVO.datasetPath = os.path.join(app.config['UPLOAD_FOLDER'])

    file.save(os.path.join(app.config['UPLOAD_FOLDER'],datasetVO.datasetName))
    datasetVO.datasetDescription = request.form['datasetDescription']
    datasetVO.datasetActiveStatus='activate'
    datasetDAO.insertDataset(datasetVO)

    return  render_template("admin/addDataset.html")




@app.route('/viewDataset')
def viewDataset():
    datasetDAO=DatasetDAO()
    datasetVO=DatasetVO()
    datasetDict=datasetDAO.viewDataset(datasetVO)
    return render_template('admin/viewDataset.html',datasetDict=datasetDict)


@app.route('/deleteDataset',methods=['get'])
def deleteDataset():
    datasetDAO=DatasetDAO()
    datasetVO=DatasetVO()
    datasetVO.datasetId=request.args.get('datasetId')
    datasetVO.datasetActiveStatus="deactive"
    datasetDAO.deleteDataset(datasetVO)

    return redirect(url_for("viewDataset"))