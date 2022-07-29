import pandas as pd
import streamlit as st
df = pd.read_csv('test1.csv')
st.write(df)