engine = create_engine(
      "mysql+pymysql://root:password@localhost/db?host=localhost?port=3306")


'''
engine = create_engine("mysql+pymysql://sylvain:passwd@localhost/db",
                       connect_args= dict(host='localhost', port=3306))
'''

 conn.execute("SELECT host FROM INFORMATION_SCHEMA.PROCESSLIST WHERE ID = CONNECTION_ID()").fetchall()
[('localhost:54164',)]

conn = engine.connect()