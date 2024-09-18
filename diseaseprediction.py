from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import csv,numpy as np,pandas as pd
import os

global ret_doc

data = pd.read_csv(os.path.join( "Training.csv"))
data2 = pd.read_csv(os.path.join( "DoctorDataset.csv"))
df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)
cols = df.columns
cols = cols[:-1]
x = df[cols]
y = df['prognosis']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

dt = RandomForestClassifier()
clf_dt=dt.fit(x_train,y_train)

# dt = DecisionTreeClassifier()
# clf_dt=dt.fit(x_train,y_train)

indices = [i for i in range(134)]
symptoms = df.columns.values[:-1]

dictionary = dict(zip(symptoms,indices))


# symptoms = []

# for i in range(5):
#     a = input('Enter symptom')
#     symptoms.append(a)


# def running_sym(symptoms):
#     user_input_label = [0 for i in range(132)]
#     for i in symptoms:
#         idx = dictionary[i]
#         user_input_label[idx] = 1

#     user_input_label = np.array(user_input_label)
#     user_input_label = user_input_label.reshape((-1,1)).transpose()

#     print(dt.predict(user_input_label))

# running_sym(symptoms)


def dosomething(symptom):
    user_input_symptoms = symptom
    user_input_label = [0 for i in range(134)]
    for i in user_input_symptoms:
        idx = dictionary[i]
        user_input_label[idx] = 1

    user_input_label = np.array(user_input_label)
    user_input_label = user_input_label.reshape((-1,1)).transpose()


    disease = dt.predict(user_input_label)
    print(disease)
    disease1 = disease[0]
    print(disease1)
    count = 0
    for i in df2['prognosis']:
        count += 1
        if disease == i:
            temp = df2.iloc[count-1]
            ret_doc = temp.Doctor

    return(disease, ret_doc)


    # return(dt.predict(user_input_label))

