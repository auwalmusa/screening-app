import streamlit as st

# Custom CSS to style the app with improved colors
st.markdown(
    """
    <style>
    body {
        background-color: #1c1e22;  /* Dark background for the app */
    }
    h1, h2, h3, .stText {
        color: #DC267F;  /* Dark pink for headers */
    }
    .stButton>button {
        background-color: #DC267F;  /* Pink button */
        color: #FFFFFF;  /* White text for the button */
        border-radius: 10px;
        border: none;
        padding: 10px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #c2156d; /* Slightly darker pink when hovered */
    }
    .stRadio>div, .stNumberInput>div {
        background-color: #2c2f33;  /* Darker grey background for inputs */
        padding: 10px;
        border-radius: 10px;
    }
    .stRadio>div, .stSelectbox>div {
        color: #FFFFFF; /* White text for inputs */
    }
    .stNumberInput>input {
        background-color: #40444b;  /* Dark grey input background */
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
