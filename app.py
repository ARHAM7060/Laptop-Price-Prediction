import streamlit as st
import pickle
import numpy as np


pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title('Laptop Price Predictor')

Company = st.selectbox('Brand',df['Company'].unique())
TypeName = st.selectbox('type',df['TypeName'].unique())
Ram = st.selectbox('ram',df['Ram'].unique())
Weight = st.number_input('Weight of the Laptop')
Touchscreen = st.selectbox('touchscreen',df['Touchscreen'].unique())
Screensize = st.number_input('Screensize')
IPS = st.selectbox('ips',df['IPS'].unique())
PPI = st.selectbox('PPI',df['PPI'].unique())
Resolution = st.selectbox('Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
CPU = st.selectbox('CPU',df['CPU Brand'].unique())
HDD = st.selectbox('HDD',df['HDD'].unique())
SSD = st.selectbox('SSD',df['SDD'].unique())
GPU = st.selectbox('GPU',df['GPU Brand'].unique())
OS = st.selectbox('OS',df['OS'].unique())

if st.button('Predict Price'):
        PPI = None
        if Touchscreen =='Yes':
                Touchscreen = int('1')
        else:
                Touchscreen = int('0')
        if IPS == 'Yes':
                IPS = int('1')
        else:
                IPS = int('0')
        X_Res = int(Resolution.split('x')[0])
        Y_Res = int(Resolution.split('x')[1])
        PPI = int(((X_Res**2 + Y_Res**2)**0.5)/Screensize)
        query = np.array([Company, TypeName, Ram, Weight, Touchscreen, IPS, PPI, CPU, HDD, SSD, GPU, OS])
        query = query.reshape(1,12)
        st.title(int(np.exp(pipe.predict(query)[0])))

