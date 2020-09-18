import requests
import json
import datetime

arr = []

def get_monthly(data):
    monthly_data = []
    for nav in data:
        if nav["date"][:2] == '15':
            monthly_data.append(nav)
    return monthly_data

with open("scheme_no.txt", "r") as f:
    for line in f:
        arr.append(int(line[:-1]))

for num in arr:
    response = requests.get("https://api.mfapi.in/mf/" + str(num))
    json_data = response.json()

    file_name = str(num)
    monthly_data = get_monthly(json_data["data"])

    with open("funds_nav/" + file_name + ".json", "w") as f:
        f.write(json.dumps(monthly_data))
    
    print("written for " + file_name)
