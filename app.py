import streamlit as st

# Title with improved size and styling
st.markdown("<h1 style='text-align: center; color: black;'>Are you eligible for screening?</h1>", unsafe_allow_html=True)

# Custom CSS for styling to match the uploaded color theme
st.markdown(
    """
    <style>
    body {
        font-family: "Arial", sans-serif;
        background-color: white;  /* White background */
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
        width: 50px; /* Set width for icons */
        margin: 0 20px; /* Adjust margin for better spacing */
    }
    .region-icon {
        width: 35px;
        margin-right: 10px;
    }
    .region-label {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
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

# Region selection with correct regions and placeholder icons
st.markdown("Where do you live?")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("<div class='region-label'><img class='region-icon' src='https://raw.githubusercontent.com/auwalmusa/screening-app/main/region_placeholder.png' /> North East</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='region-label'><img class='region-icon' src='https://raw.githubusercontent.com/auwalmusa/screening-app/main/region_placeholder.png' /> London</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='region-label'><img class='region-icon' src='https://raw.githubusercontent.com/auwalmusa/screening-app/main/region_placeholder.png' /> South East</div>", unsafe_allow_html=True)
with col4:
    st.markdown("<div class='region-label'><img class='region-icon' src='https://raw.githubusercontent.com/auwalmusa/screening-app/main/region_placeholder.png' /> Midlands</div>", unsafe_allow_html=True)

# Second row of regions
col5, col6, col7 = st.columns(3)
with col5:
    st.markdown("<div class='region-label'><img class='region-icon' src='https://raw.githubusercontent.com/auwalmusa/screening-app/main/region_placeholder.png' /> North West</div>", unsafe_allow_html=True)
with col6:
    st.markdown("<div class='region-label'><img class='region-icon' src='https://raw.githubusercontent.com/auwalmusa/screening-app/main/region_placeholder.png' /> East</div>", unsafe_allow_html=True)
with col7:
    st.markdown("<div class='region-label'><img class='region-icon' src='https://raw.githubusercontent.com/auwalmusa/screening-app/main/region_placeholder.png' /> South West</div>", unsafe_allow_html=True)

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
