# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 13:09:07 2019

@author: DiPu
"""
import pickle
import numpy as np
from datetime import datetime as dt
store=2
dept=45
week="2018-05-06"
fuel=4.78
temp=34
Type='B'
unemp=6.78
m1=0
m2=45
m3=2
m4=45
m5=12
cpi=234
IsHoliday=True
size=4567

week=dt.strptime(week,'%Y-%m-%d')            
week= week.toordinal()

y=[Type]
y=np.array(y).reshape(1,-1)
y=int(y)


x=[store,temp,fuel,m1,m2,m3,m4,m5,cpi,unemp,IsHoliday,size,week]
inp_arr=np.array(x).reshape(1,-1)

with open("label_encode_type.pickle","rb") as type_model:
    model=pickle.load(type_model)
    y[:,:]=model.transform(y[:,:])


with open("label_encode_isholiday.pickle","rb") as isholiday_model:
    x=pickle.load(isholiday_model)
    inp_arr[:,10]=x.transform(inp_arr[:,10])
    
inp_arr=np.insert(inp_arr, 11, y, axis=1)



with open("scaling.pickle","rb") as scale:
    scaler=pickle.load(scale)
    inp_arr=scaler.transform(inp_arr)
    
with open("random_forest_regressor.pickle","rb") as regressor_model:
    regressor=pickle.load(regressor_model)
    output=regressor.predict(inp_arr)
