import streamlit as st

# Title
st.title("Are you eligible for screening?")

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
    </style>
    """,
    unsafe_allow_html=True
)

# Display icons for Woman and Man
col1, col2 = st.columns([1, 1])
with col1:
    st.image("woman_icon.png", width=50)
    gender = st.radio("", ["Woman"], index=0)
with col2:
    st.image("man_icon.png", width=50)
    gender = st.radio("", ["Man"])

# Age input
age = st.number_input("Age:", min_value=0, max_value=100, step=1)

# Region selection with custom icons (if available)
region = st.radio("Where do you live?", 
                  ["England", "Wales", "N. Ireland", "Scotland"])

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
