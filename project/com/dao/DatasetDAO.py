from project.com.dao import *

class DatasetDAO:
    def insertDataset(self,DatasetVO):
        connection=conn_db()
        cursor1=connection.cursor()
        cursor1.execute('INSERT into datasetmaster(datasetName,datasetPath,datasetDescription,datasetActiveStatus) VALUES("'+DatasetVO.datasetName+'","'+DatasetVO.datasetPath+'","'+DatasetVO.datasetDescription+'","'+DatasetVO.datasetActiveStatus+'")' )
        connection.commit()
        cursor1.close()
        connection.close()

    def viewDataset(self, DatasetVO):
        connection = conn_db()
        cursor1 = connection.cursor()
        cursor1.execute("SELECT * FROM datasetmaster WHERE datasetActiveStatus='active' ")
        datasetDict=cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return datasetDict

    def deleteDataset(self, datasetVO):
        connection = conn_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE datasetmaster SET datasetActiveStatus='"+datasetVO.datasetActiveStatus+"' WHERE datasetId='"+datasetVO.datasetId+"' ")
        connection.commit()
        cursor1.close()
        connection.close()
