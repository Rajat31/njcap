import requests
import json
import datetime

ctr = 1

arr = []

with open("growth_fund_nums.txt", "r") as f:
    for line in f:
        arr.append(int(line[:-1]))

with open("fund_house.txt", "w") as fund_house:
    with open("scheme_type.txt", "w") as scheme_type:
        with open("scheme_category.txt", "w") as scheme_category:
            with open("scheme_no.txt", "w") as scheme_no:
                with open("scheme_name.txt", "w") as scheme_name:
                    for num in arr:
                        response = requests.get("https://api.mfapi.in/mf/" + str(num))
                        json_data = response.json()

                        today = datetime.date.today()

                        five_days_ago = today - datetime.timedelta(days=5)
                        
                        data_date = datetime.datetime.strptime(json_data["data"][0]["date"], "%d-%m-%Y").strftime("%Y-%m-%d")
                        date_object = datetime.datetime.strptime(data_date, '%Y-%m-%d').date()

                        last_data_date = datetime.datetime.strptime(json_data["data"][-1]["date"], "%d-%m-%Y").strftime("%Y-%m-%d")
                        last_date_object = datetime.datetime.strptime(last_data_date, '%Y-%m-%d').date()
                        
                        if (date_object - five_days_ago).days >= 0 and (five_days_ago - last_date_object).days >= 1460:
                            print("%s. %s (%s)" %(str(ctr), json_data["meta"]["scheme_name"], str(num)))
                            ctr += 1
                            scheme_no.write('%d\n' % json_data["meta"]["scheme_code"])
                            fund_house.write('%s\n' % json_data["meta"]["fund_house"])
                            scheme_type.write('%s\n' % json_data["meta"]["scheme_type"])
                            scheme_category.write('%s\n' % json_data["meta"]["scheme_category"])
                            scheme_name.write('%s\n' % json_data["meta"]["scheme_name"])