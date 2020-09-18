import pyodbc
SERVER = 'mf-server.database.windows.net'
DB_NAME = 'mutual-fund-names'
USERNAME = 'njcap-admin'
PASSWORD = 'Naman-ka-gyan'   
DRIVER= '{ODBC Driver 17 for SQL Server}'

def test_connection():
    with pyodbc.connect('DRIVER='+DRIVER+';SERVER='+SERVER+';PORT=1433;DATABASE='+DB_NAME+';UID='+USERNAME+';PWD='+ PASSWORD) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM TEST_TABLE")
            row = cursor.fetchone()
            while row:
                print("----------------------< TEST DATA >-------------------------")
                print (str(row[0]) + " " + str(row[1]))
                print("------------------------------------------------------------")
                row = cursor.fetchone()

def dump_data():
    scheme_no = prepare_scheme_nos()
    scheme_name = prepare_scheme_name()
    scheme_category = prepare_scheme_category()
    scheme_type = prepare_scheme_type()
    fund_house = prepare_fund_house()

    # print("{} | {} | {} | {} | {}".format(scheme_no[0], scheme_name[0], scheme_category[0], scheme_type[0], fund_house[0]))

    with pyodbc.connect('DRIVER='+DRIVER+';SERVER='+SERVER+';PORT=1433;DATABASE='+DB_NAME+';UID='+USERNAME+';PWD='+ PASSWORD) as conn:
        with conn.cursor() as cursor:
            for index in range(len(scheme_no)):
                cursor.execute("INSERT INTO FUNDS_DATA VALUES ({}, \'{}\', \'{}\', \'{}\', \'{}\')".format(str(scheme_no[index]),
                    scheme_name[index],
                    scheme_category[index],
                    scheme_type[index],
                    fund_house[index]))
                print("{} done.".format(str(index+1)))


def prepare_scheme_nos():
    scheme_no = []
    with open("scheme_no.txt", "r") as f:
        nos = f.readlines()
    for line in nos:
        scheme_no.append(int(line.strip().replace(r"'", r"''")))
    return scheme_no

def prepare_fund_house():
    fund_house = []
    with open("fund_house.txt", "r") as f:
        nos = f.readlines()
    for line in nos:
        fund_house.append(line.strip().replace(r"'", r"''"))
    return fund_house

def prepare_scheme_category():
    scheme_category = []
    with open("scheme_category.txt", "r") as f:
        nos = f.readlines()
    for line in nos:
        scheme_category.append(line.strip().replace(r"'", r"''"))
    return scheme_category

def prepare_scheme_name():
    scheme_name = []
    with open("scheme_name.txt", "r") as f:
        nos = f.readlines()
    for line in nos:
        scheme_name.append(line.strip().replace(r"'", r"''"))
    return scheme_name

def prepare_scheme_type():
    scheme_type = []
    with open("scheme_type.txt", "r") as f:
        nos = f.readlines()
    for line in nos:
        scheme_type.append(line.strip().replace(r"'", r"''"))
    return scheme_type