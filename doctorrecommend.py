import csv,numpy as np,pandas as pd
import os

data = pd.read_csv(( "DoctorDataset.csv"))
df = pd.DataFrame(data)

disease = 'Acne'
count = 0

for i in df['prognosis']:
    count += 1
    if disease == i:
        temp = df.iloc[count-1]
        var = temp.Doctor
        print(temp)
        print(var)




# for i in df['prognosis']:
#     print(i)
