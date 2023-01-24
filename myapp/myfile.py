import pandas as pd
from myapp.models import drugInterectionTable
from django.db.models import Q

df1 = pd.read_csv("myapp/ddinter_downloads_code_A.csv")
df2 = pd.read_csv("myapp/ddinter_downloads_code_B.csv")
df3 = pd.read_csv("myapp/ddinter_downloads_code_D.csv")
df4 = pd.read_csv("myapp/ddinter_downloads_code_H.csv")
df5 = pd.read_csv("myapp/ddinter_downloads_code_L.csv")
df6 = pd.read_csv("myapp/ddinter_downloads_code_P.csv")
df7 = pd.read_csv("myapp/ddinter_downloads_code_R.csv")
df8 = pd.read_csv("myapp/ddinter_downloads_code_V.csv")

frames = [df1, df2, df3, df4, df5, df6, df7, df8]
df = pd.concat(frames)
print(df.shape)

final_df = df.drop_duplicates()
print(final_df.shape)

    # if drugLevelTable.objects.filter(Q(drug1_id = file1.iloc[i, 0]) & Q(drug2_id = file1.iloc[i, 2])):
    #     continue
    # else:

for i in range(len(final_df)):
    drugInterectionTable.objects.create(
        drug1_id = final_df.iloc[i, 0],
        drug1_name = final_df.iloc[i, 1],
        drug2_id = final_df.iloc[i, 2],
        drug2_name = final_df.iloc[i, 3],
        level = final_df.iloc[i, 4],
    )
