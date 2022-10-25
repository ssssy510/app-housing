import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data(1990) by sssy')

df = pd.read_csv('housing.csv')

price_slider = st.slider('Median House Price', 0, 500001, 200000)
df = df[df.median_house_value >= price_slider]

location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(), 
     df.ocean_proximity.unique())  
df = df[df.ocean_proximity.isin(location_filter)]

income_filter = st.sidebar.radio(
    'Choose income level', 
    ('Low', 'Median', 'High')
)
if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Median':
    df = df[df.median_income > 2.5 & df.median_income < 4.5]
elif income_filter == 'High':
    df = df[df.median_income > 4.5]

st.map(df)
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots()
ax.hist(df['median_house_value'], bins=30)
st.pyplot(fig)