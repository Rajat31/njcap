import requests
import json
import datetime
import pyodbc

SERVER = 'mf-server.database.windows.net'
DB_NAME = 'mutual-fund-names'
USERNAME = 'njcap-admin'
PASSWORD = 'Naman-ka-gyan'   
DRIVER= '{ODBC Driver 17 for SQL Server}'

counter = 100000

ctr = 1

with open("growth_fund_nums.txt", "w") as num_file:
    with open("growth_fund_names.txt", "w") as name_file:
        while counter < 1000000:
            response = requests.get("https://api.mfapi.in/mf/" + str(counter))
            json_data = response.json()
            if len(json_data['meta']):
                scheme_name = json_data['meta']['scheme_name']
                if scheme_name.lower().find('growth') >= 0:
                    print("%s. %s (%s)" %(str(ctr), scheme_name, str(counter)))
                    ctr += 1
                    num_file.write('%d\n' % counter)
                    name_file.write('%s\n' % scheme_name)
            counter += 1