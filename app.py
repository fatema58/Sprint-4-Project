import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

st.title("Sprint-4-Project")
st.header("Introduction")
st.text("This project will analyze vehicles_US dataframe to analyze the number of days a vehicle is advertised")

df = pd.read_csv("vehicles_us.csv") 
# To display the DataFrame in Streamlit
st.dataframe(df)

st.header("Age of a vehicle when the ad was listed")
df['date_posted']= pd.to_datetime(df['date_posted'])
df['year_posted'] = df['date_posted'].dt.year
df['month_posted'] = df['date_posted'].dt.month
df['dow_posted'] = df['date_posted'].dt.dayofweek
df['age_in_years'] = (df['date_posted'] - pd.to_datetime(df['model_year'], format='%Y')) / np.timedelta64(1, 'D') / 365.25
fig2 = px.histogram(df, x='age_in_years', labels={'age_in_years':'Age in Years'})
st.plotly_chart(fig2)
st.text("The average and median age of a vehicle in this data set is similar - around 8-9 years. We also see quite a long tail of large values, we will remove those that we consider outliers in the next section.")


st.header("Age vs Price")
fig1 = px.scatter(df, x='price', y='age_in_years', 
                 title='Age vs Price of vehicles',
                 labels={'price': 'Price', 'age_in_years': 'Age in years'},
                 template='plotly_white')
st.plotly_chart(fig1)
st.text("The data reflects real life situation: the more recent a car's model, the higher its price.")

display_text = st.checkbox('Display greeting text')
if display_text:
    st.write('Hello, welcome to my Streamlit app!')
else:
    st.write('Select the checkbox to display the greeting text.')


