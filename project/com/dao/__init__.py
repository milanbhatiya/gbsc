import pymysql

def conn_db():
    return pymysql.connect('localhost',
                           'root',
                           'root',
                           'gesturebasedsmartcommunicator',
                           cursorclass=pymysql.cursors.DictCursor)