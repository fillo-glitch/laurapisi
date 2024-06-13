import joblib
import pandas as pd
import streamlit as st
import numpy as np



model_pipe = joblib.load('pinguinipipe.pkl')
print('Model loaded successfully')


island = st.selectbox('inserire isola',['Torgensen','Dream','Biscoe'])
bill_length_mm = st.number_input("Please inserire lunghezza becco",20.0,60.0,30.0)
bill_depth_mm = st.number_input("Please inserire profondità becco",10.0,30.0,15.0)
flipper_length_mm = st.number_input("Please inserire pinna", 5.0,40.0,15.0)
body_mass_g = st.number_input("Please inserire percentuale grasso", 0.0,40.0,10.0)
sex = st.selectbox('inserire sesso',['female','male'])


data = {
        "island": [island],
        "bill_length_mm": [bill_length_mm],
        "bill_depth_mm": [bill_depth_mm],
        "flipper_length_mm":[flipper_length_mm],
        "body_mass_g": [body_mass_g],
        "sex": [sex],
        }

input_df = pd.DataFrame(data)
res = model_pipe.predict(input_df).astype(int)[0]
print(res)

classes = {0:'Adelie',
           1:'Gentoo',
           2:'Chinstrap',
           }

y_pred = classes[res]
if st.button('Predicition'):
    st.success(f'species di pinguini  {y_pred}')