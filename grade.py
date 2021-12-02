import streamlit as st
import pandas as pd

st.write("""
# Data Topic: Analysis of registration data in the elective subject

show information about the subject that get the most  A grade
""")



data_sample = pd.read_csv('Final_form.csv')
# df = pd.concat([df,data_sample],axis=0)

st.write(data_sample)