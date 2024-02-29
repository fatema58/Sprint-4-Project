import pandas as pd
import streamlit as st
import plotly as pt
import matplotlib.pyplot as plt

df = pd.read_csv('vehicles_us.csv')

def brand(row):
    """
    Takes in a vehicle's model and returns its brand
    """
    
    model = row['model']
    model_split = model.split(' ')
    brand = model_split[0]
    return brand

df['brand'] = df.apply(brand, axis=1)

st.title("Sprint-4-Project")
st.header("Introduction")
st.text("This project will analyze vehicles_US dataframe to analyze the number of days a vehicle is advertised")

st.header("Hypothesis")
st.text("")

st.write(df)
