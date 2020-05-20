from flask import Flask,render_template,request
import pickle 
import numpy as np

model = pickle.load(open(r'C:\Users\HP\Desktop\Liver Patient Analysis\flask\liver.pkl','rb'))

app =Flask (__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login',methods=['POST'])
def login():
     Age =request.form['Age']
     Gender= request.form['Gender']
     Total_Bilirubin= request.form['Total_Bilirubin']
     Alkaline_Phosphotase= request.form['Alkaline_Phosphotase']
     Alamine_Aminotransferase= request.form['Alamine_Aminotransferase']
     Aspartate_Aminotransferase= request.form['Aspartate_Aminotransferase']
     Total_Protiens= request.form['Total_Protiens']
     Albumin_and_Globulin_Ratio= request.form['	Albumin_and_Globulin_Ratio']
     
     strength = [[Age,Gender,Total_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin_and_Globulin_Ratio]]
     y_pred = model.predict(np.array(strength))
     
     
     return render_template("index.html",showcase =y_pred)
 

if __name__=='__main__':
    app.run(debug =False)
