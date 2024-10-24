import streamlit as st

# Title
st.title("Eligibility for Screening")

# Gender selection
gender = st.radio("Select your gender:", ["Woman", "Man"])

# Age input
age = st.number_input("Enter your age:", min_value=0, max_value=100, step=1)

# Region selection
region = st.radio("Where do you live?", 
                  ["North East", "London", "South East", "Midlands", "North West", "East", "South West"])

# Function to check eligibility
def check_eligibility(gender, age):
    if gender == "Man" and age >= 40:
        return "You are eligible."
    elif gender == "Woman" and age >= 30:
        return "You are eligible."
    else:
        return "You are not eligible."

# Submit button
if st.button("Am I eligible?"):
    eligibility_message = check_eligibility(gender, age)
    st.write(eligibility_message)
