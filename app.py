import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

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
show_trendline = st.checkbox('Show Trendline')
# Scatter plot
if show_trendline:
    fig1 = px.scatter(df, x='price', y='age_in_years', 
                      trendline='ols',  # Ordinary Least Squares regression
                      title='Age vs Price of vehicles',
                      labels={'price': 'Price', 'age_in_years': 'Age in years'},
                      template='plotly_white')
else:
    fig1 = px.scatter(df, x='price', y='age_in_years', 
                      title='Age vs Price of vehicles',
                      labels={'price': 'Price', 'age_in_years': 'Age in years'},
                      template='plotly_white')
st.plotly_chart(fig1)
st.text("The data reflects real life situation: the more recent a car's model, the higher its price.")


st.header('Dsiplaying days_listed column as a histogram using matplotlib')
df['days_listed'].hist(bins=100)
plt.title("Length of a vehicle's ad listed, in days")
plt.xlabel('days listed')
plt.ylabel('no of vehicles');
st.text('A lifetime of an ad in this dataset ranges from 0 up to around 250 days, the distribution is skewed towards large positive values. A typical ad is placed for around 30-40 days, so around 1 month. Vehicles with higher values can be considered outliers')