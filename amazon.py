import streamlit as st
import pandas as pd

adf = pd.read_csv("a.csv")

st.title("Amazon Spend Report")
adf