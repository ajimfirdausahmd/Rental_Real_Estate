import streamlit as st
import pandas as pd
from sklearn import datasets

st.write("""
## Rental Real Estate Calculator 
         
    This app calcuate montage payment
""" )

st.sidebar.header('User Input Calculate')

def user_input_features():
    House_Price =  st.sidebar.slider('House_Price',200000,20000000,500000)
    Down_Payment =  st.sidebar.slider('Down_Payment',1000,10000,3000)
    Principle =  st.sidebar.slider('Principle',40000,400000,100000)
    Long_Term_in_years =  st.sidebar.slider('Long_Term_in_years',1,30,30)
    Annual_Interest =  st.sidebar.slider('Annual_Interest',0.0,10.0,5.0)
    Monthly_Taxes =  st.sidebar.slider('Monthly_Texas',0,1000,250)
    data = {'House_Price': House_Price,
            'Down_Payment': Down_Payment,
            'Principle': Principle,
            'Long_Term_in_years': Long_Term_in_years,
            'Annual_Interest': Annual_Interest,
            'Monthly_Taxes' : Monthly_Taxes}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('House Price:')
st.subheader('Down payment (20%):')
st.subheader('Principle:')
st.subheader('Monthly Mortgage:')
st.subheader('Monthly Rent-To-Value:')
st.subheader('Annual Gross Rental:')
st.subheader('Annual Profit:')



