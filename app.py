import streamlit as st

# Title
st.title("Eligibility Checker")

# Input for region
region = st.selectbox("Where do you live?", 
                      ["North East", "London", "South East", "Midlands", "North West", "East", "South West"])

# Input for gender
gender = st.selectbox("What is your gender?", ["Man", "Woman"])

# Input for age
age = st.number_input("Enter your age", min_value=0, max_value=100, step=1)

# Eligibility check
def check_eligibility(gender, age):
