# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 18:46:44 2019

@author: DiPu
"""

from flask import Flask, request, render_template, url_for
import numpy as np
import pickle
from datetime import datetime as dt
app = Flask(__name__)


@app.route("/start")
def first():
    return render_template("first.html")

@app.route("/main",methods=["POST"])
def home():
    return render_template("index.html")

@app.route("/result",methods=["POST"])
def predict():
    user_data=request.form
    store=user_data["Store_No"]
    dept=user_data["Dept_no"]
    week=user_data["Weekly_day"]
    fuel=user_data["Fuel_price"]
    temp=user_data["Temp"]
    Type=user_data["Type"]
    unemp=user_data["Unemployment_rate"]
    m1=user_data["Markdown1"]
    m2=user_data["Markdown2"]
    m3=user_data["Markdown3"]
    m4=user_data["Markdown4"]
    m5=user_data["Markdown5"]
    cpi=user_data["CPI"]
    holiday=user_data["holiday"]
    size=user_data["Size"]
    week=dt.strptime(week,'%Y-%m-%d')            
    week= week.toordinal()
    
    
    x=[store,temp,fuel,m1,m2,m3,m4,m5,cpi,unemp,Type,holiday,size,week]
    inp_arr=np.array(x).reshape(1,-1)
    
#    print("[BEFORE]:  " + str(inp_arr))
    
#    y=[Type]
#    y=np.array(y).reshape(1,-1)
    
    with open("label_encode_type.pickle","rb") as type_model:
        model=pickle.load(type_model)
        inp_arr[:,10]=model.transform(inp_arr[:,10])
        
#    print("[AFTER 1] : "+ str(inp_arr))
#    y=int(y)
#    holiday=holiday.astype(bool)
#    
#    x=[store,temp,fuel,m1,m2,m3,m4,m5,cpi,unemp,holiday,size,week]
#    inp_arr=np.array(x).reshape(1,-1)
    
    if holiday == "True":
        holiday = True
    else:
        holiday = False
        
    
    with open("label_encode_isholiday.pickle","rb") as isholiday_model:
        x=pickle.load(isholiday_model)
        tmp = x.transform(np.array([holiday]))
        inp_arr[:,11] = tmp
        
#    inp_arr=np.insert(inp_arr, 11, y, axis=1)
    
    inp_arr = inp_arr.astype(np.int64)
#    print("[FINAL] : " + str(inp_arr))
    
    
    with open("scaling.pickle","rb") as scale:
        scaler=pickle.load(scale)
        inp_arr=scaler.transform(inp_arr)
        
    with open("random_forest_regressor.pickle","rb") as regressor_model:
        regressor=pickle.load(regressor_model)
        output=regressor.predict(inp_arr)
    return render_template('response.html', status=output)

if __name__ == "__main__":
    app.run(debug=True, port=5500)
