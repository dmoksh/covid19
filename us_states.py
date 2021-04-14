import streamlit as st
import pandas as pd


#read csv data from nytimes githib repository
df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")

#write title
st.title("COVID data by US States")

#create bar chart 
st.bar_chart(df.groupby(['state'])['cases'].sum())

