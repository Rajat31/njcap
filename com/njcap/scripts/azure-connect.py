import pyodbc
SERVER = 'mf-server.database.windows.net'
DB_NAME = 'mutual-fund-names'
USERNAME = 'njcap-admin'
PASSWORD = 'Naman-ka-gyan'   
DRIVER= '{ODBC Driver 17 for SQL Server}'

def test_connection():
    with pyodbc.connect('DRIVER='+DRIVER+';SERVER='+SERVER+';PORT=1433;DATABASE='+DB_NAME+';UID='+USERNAME+';PWD='+ PASSWORD) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM MF_NAMES_ID")
            row = cursor.fetchone()
            while row:
                print (str(row[0]) + " " + str(row[1]))
                row = cursor.fetchone()