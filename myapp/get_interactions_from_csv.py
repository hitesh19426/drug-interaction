import pandas as pd

data = pd.read_csv("/home/hiteshgarg/mysite/myapp/Drug Availibity in DDInter.csv")

print(data["Drg_name"])

for drug in data["Drg_name"]:
    print("<li>" + str(drug) + "</li>")