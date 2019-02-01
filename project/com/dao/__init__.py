import pymysql

def conn_db():
    return pymysql.connect('localhost',
                           'root',
                           '12345678',
                           'gbsc',
                           cursorclass=pymysql.cursors.DictCursor)