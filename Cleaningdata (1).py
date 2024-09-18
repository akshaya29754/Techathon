
# Import Dependencies
import csv
import pandas as pd
import numpy as np
from collections import defaultdict
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

# Read Raw Dataset
df = pd.read_excel('raw_data.xlsx')

df.head()

# Fill all NaN with the values above
data = df.fillna(method='ffill')

data.head()

# Process Disease and Symptom Names
def process_data(data):
    data_list = []
    data_name = data.replace('^','_').split('_')
    n = 1
    for names in data_name:
        if (n % 2 == 0):
            data_list.append(names)
        n += 1
    return data_list

# Data Cleanup
disease_list = []
disease_symptom_dict = defaultdict(list)
disease_symptom_count = {}
count = 0

for idx, row in data.iterrows():
    
    # Get the Disease Names
    if (row['Disease'] !="\xc2\xa0") and (row['Disease'] != ""):
        disease = row['Disease']
        disease_list = process_data(data=disease)
        count = row['Count of Disease Occurrence']

    # Get the Symptoms Corresponding to Diseases
    if (row['Symptom'] !="\xc2\xa0") and (row['Symptom'] != ""):
        symptom = row['Symptom']
        symptom_list = process_data(data=symptom)
        for d in disease_list:
            for s in symptom_list:
                disease_symptom_dict[d].append(s)
            disease_symptom_count[d] = count

# See that the data is Processed Correctly
disease_symptom_dict

# Count of Disease Occurence w.r.t each Disease
disease_symptom_count

# Save cleaned data as CSV
f = open('cleaned_data.csv', 'w')

with f:
    writer = csv.writer(f)
    for key, val in disease_symptom_dict.items():
        for i in range(len(val)):
            writer.writerow([key, val[i], disease_symptom_count[key]])

# Read Cleaned Data as DF
df = pd.read_csv('cleaned_data.csv')
df.columns = ['disease', 'symptom', 'occurence_count']
df.head()

# Remove any rows with empty values
df.replace(float('nan'), np.nan, inplace=True)
df.dropna(inplace=True)

from sklearn import preprocessing

n_unique = len(df['symptom'].unique())
n_unique

df.dtypes

# Encode the Labels
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(df['symptom'])
print(integer_encoded)

# One Hot Encode the Labels
onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
print(onehot_encoded)

onehot_encoded[0]

len(onehot_encoded[0])

cols = np.asarray(df['symptom'].unique())
cols

# Create a new dataframe to save OHE labels
df_ohe = pd.DataFrame(columns = cols)
df_ohe.head()

for i in range(len(onehot_encoded)):
    df_ohe.loc[i] = onehot_encoded[i]

df_ohe.head()

len(df_ohe)

# Disease Dataframe
df_disease = df['disease']
df_disease.head()

# Concatenate OHE Labels with the Disease Column
df_concat = pd.concat([df_disease,df_ohe], axis=1)
df_concat.head()

df_concat.drop_duplicates(keep='first',inplace=True)

df_concat.head()

len(df_concat)

cols = df_concat.columns
cols

cols = cols[1:]

# Since, every disease has multiple symptoms, combine all symptoms per disease per row
df_concat = df_concat.groupby('disease').sum()
df_concat = df_concat.reset_index()
df_concat[:5]

len(df_concat)

df_concat.to_csv("Training.csv", index=False)

# One Hot Encoded Features
X = df_concat[cols]

# Labels
y = df_concat['disease']

