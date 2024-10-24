import streamlit as st

# Title with improved size and styling
st.markdown("<h1 style='text-align: center; color: #DC267F;'>Are you eligible for screening?</h1>", unsafe_allow_html=True)

# Custom CSS for styling to match the uploaded image
st.markdown(
    """
    <style>
    body {
        font-family: "Arial", sans-serif;
    }
    .stRadio>div>div {
        padding: 10px;
    }
    .stRadio label {
        font-size: 16px;
        font-weight: normal;
    }
    .stButton>button {
        background-color: #DC267F;
        color: white;
        font-size: 18px;
        padding: 10px;
        width: 100%;
        border-radius: 10px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #c2156d;
    }
    .stMarkdown a {
        color: #4B0082;
        font-weight: bold;
    }
    .icon-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .gender-icon {
        width: 70px; /* Set a bigger width for better visibility */
        margin: 0 30px; /* Adjust margin for better spacing */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display icons for Woman and Man using raw GitHub URLs, improved layout
st.markdown("<div class='icon-container'><img class='gender-icon' src='https://raw.githubusercontent.com/auwalmusa/screening-app/main/woman.png' /><img class='gender-icon' src='https://raw.githubusercontent.com/auwalmusa/screening-app/main/man.png' /></div>", unsafe_allow_html=True)

# Gender selection below the icons
col1, col2 = st.columns(2)
with col1:
    gender = st.radio("", ["Woman"], index=0)
with col2:
    gender = st.radio("", ["Man"])

# Information for trans and non-binary individuals
st.markdown("[Information for trans and non-binary individuals](https://example.com)")  # Replace with actual link

# Age input
age = st.number_input("Age:", min_value=0, max_value=100, step=1)

# Region selection with corrected regions
region = st.radio("Where do you live?", 
                  ["North East", "London", "South East", "Midlands", "North West", "East", "South West"])

# Function to check eligibility
def check_eligibility(gender, age):
    if gender == "Man" and age < 40:
        return "You are eligible."
    elif gender == "Woman" and age >= 30:
        return "You are eligible."
    else:
        return "You are not eligible."

# Submit button, centered and styled
if st.button("Am I eligible?"):
    eligibility_message = check_eligibility(gender, age)
    st.write(eligibility_message)
