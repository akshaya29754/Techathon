import csv
from sqlite3 import Cursor
from flask import Flask, render_template,request,redirect,url_for,session
import diseaseprediction
from flask_mysqldb import MySQL
import mysql.connector
import os

app = Flask(__name__)
app.secret_key=os.urandom(24)

conn=mysql.connector.connect(host="localhost", user="root", password="", database="test")
cursor=conn.cursor()

@app.route('/homedoctor1' )
def homedoctorpage(): 
    cursor.execute("select * from disease") 
    data = cursor.fetchall() #data from database 
    return render_template("homedoctor1.html", value=data) 


with open('Testing.csv', newline='') as f:
        reader = csv.reader(f)
        symptoms = next(reader)
        symptoms = symptoms[:len(symptoms)-1]
@app.route('/homepatient1', methods=['GET'])
def dropdown():
        return render_template('homepatient1.html', symptoms=symptoms)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signindoc')
def signindoc():
    
    return render_template('signindoc.html')

@app.route('/signinpat')
def signinpat():
    return render_template('signinpat.html')

@app.route('/homedoctor' )
def homedoctor():
    if 'user_id' in session:
        return render_template('homedoctor.html')
    else:
        return redirect('/signindoc')

@app.route('/homepatient' )
def homepatient():
    if 'user_id' in session:
        return render_template('homepatient.html')
    else:
        return redirect('/signinpat')

@app.route('/loginvalidate_doc', methods=['POST'])
def loginvalidate_doc():
    Username=request.form.get('Username')
    password=request.form.get('password')

    cursor.execute("""SELECT * FROM  `doctor` WHERE `Username` LIKE '{}' AND `password` LIKE '{}' """.format(Username,password))
    users=cursor.fetchall()
    if len(users)>0:
      session['user_id']=users[0][0]
      return redirect('/homedoctor')
    else:
        return redirect('/signindoc')

@app.route('/loginvalidate_pat', methods=['POST'])
def loginvalidate_pat():
    Username=request.form.get('Username')
    password=request.form.get('password')

    cursor.execute("""SELECT * FROM  `patient` WHERE `Username` LIKE '{}' AND `password` LIKE '{}' """.format(Username,password))
    users=cursor.fetchall()
    if len(users)>0:
      session['user_id']=users[0][0]
      return redirect('/homepatient')
    else:
        return redirect('/signinpat')        

@app.route('/add_doc', methods=['POST'])
def add_doc():
    Username=request.form.get('Username')
    email=request.form.get('email')
    password=request.form.get('password')
    specialization=request.form.get('specialization')

    cursor.execute("""INSERT INTO `doctor` (`id`,`Username`,`email`,`password`,`specialization`) VALUES(NULL,'{}','{}','{}','{}')""".format(Username,email,password,specialization))
    conn.commit()
    return redirect('/signindoc')

@app.route('/add_pat', methods=['POST'])
def add_pat():
    Username=request.form.get('Username')
    email=request.form.get('email')
    password=request.form.get('password')
    contact=request.form.get('contact')

    cursor.execute("""INSERT INTO `patient` (`id`,`Username`,`email`,`password`,`contact`) VALUES(NULL,'{}','{}','{}','{}')""".format(Username,email,password,contact))
    conn.commit()
    return redirect('/signinpat') 

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/Doctors')
def Doctors():
    return render_template('Doctors.html')

@app.route('/homepatient2')
def homepatient2():
    return render_template('homepatient2.html')   

@app.route('/homedoctor1')
def homedoctor1():
    return render_template('homedoctor1.html')   

# @app.route('/diseasepredict')
# def diseasepredicthtml():
#     return render_template('diseasepredict.html')  

@app.route('/logoutdoc')
def logoutdoc():
    session.pop('user_id')
    return redirect('signindoc')

@app.route('/logoutpat')
def logoutpat():
    session.pop('user_id')
    return redirect('signinpat')


@app.route('/disease_predict', methods=['POST'])
def disease_predict():
    selected_symptoms = []
    if(request.form['Symptom1']!="") and (request.form['Symptom1'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom1'])
    if(request.form['Symptom2']!="") and (request.form['Symptom2'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom2'])
    if(request.form['Symptom3']!="") and (request.form['Symptom3'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom3'])
    if(request.form['Symptom4']!="") and (request.form['Symptom4'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom4'])
    if(request.form['Symptom5']!="") and (request.form['Symptom5'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom5'])

    disease1, ret_doc = diseaseprediction.dosomething(selected_symptoms)
    print(ret_doc)
    
    name=request.form.get('name')
    Symptom1=request.form.get('Symptom1')
    Symptom2=request.form.get('Symptom2')
    Symptom3=request.form.get('Symptom3')
    Symptom4=request.form.get('Symptom4')
    Symptom5=request.form.get('Symptom5')
    disease= disease1[0];
    
    cursor.execute("""INSERT INTO `disease` (`name`,`Symptom1`,`Symptom2`,`Symptom3`,`Symptom4`,`Symptom5`,`disease`) VALUES('{}','{}','{}','{}','{}','{}','{}')""".format(name,Symptom1,Symptom2,Symptom3,Symptom4,Symptom5, disease))
    conn.commit()

    return render_template('diseasepredict.html',disease=disease1, doctor = ret_doc, symptoms=symptoms)



if __name__ == '__main__':
    app.run(debug=True)