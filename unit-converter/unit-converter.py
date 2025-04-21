import streamlit as st

# Set page configuration
st.set_page_config(page_title="Unit Converter App", page_icon="♻️")

# Custom CSS for styling
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to right, #2f2f2f, #121212);
            color: #ffffff;
        }
        header, .css-1v3fvcr, .css-1d391kg {
            display: none !important;
        }
        .stButton>button {
            background: #3a3a3a;
            color: white;
            padding: 5px 17px;
            font-size: 16px;
            cursor: pointer;
            border: none;
        }
        .stButton>button:hover {
            background: #ff7e5f;
        }
        .stNumberInput input {
            border: 2px solid #ff7e5f;
            color: white;
            background-color: #2f2f2f;
        }
        .stNumberInput input:focus {
            border: 2px solid #ffffff;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1 style='text-align: center; color: white;'>♻️ Unit Converter App</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Quick and Easy Conversion of Length, Weight, and Time</h3>", unsafe_allow_html=True)

# Introduction
st.markdown("<p style='text-align: center; font-size: 18px; color: white;'>Welcome! Choose a category, input a value, and view the conversion result instantly.</p>", unsafe_allow_html=True)

# Category Selection
st.markdown("<p style='color: white; font-weight: bold;'>💡 Choose a category</p>", unsafe_allow_html=True)
category = st.selectbox("", ["Length", "Weight", "Time"], key="category")

# Unit Selection
if category == "Length":
    st.markdown("<p style='color: white; font-weight: bold;'>⏱️ Select Conversion</p>", unsafe_allow_html=True)
    unit = st.selectbox("", ["Kilometers to Miles", "Miles to Kilometers"], key="unit_length")
elif category == "Weight":
    st.markdown("<p style='color: white; font-weight: bold;'>⏱️ Select Conversion</p>", unsafe_allow_html=True)
    unit = st.selectbox("", ["Kilograms to pounds", "Pounds to kilograms"], key="unit_weight")
elif category == "Time":
    st.markdown("<p style='color: white; font-weight: bold;'>⏱️ Select Conversion</p>", unsafe_allow_html=True)
    unit = st.selectbox("", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"], key="unit_time")

# Value Input
st.markdown("<p style='color: white; font-weight: bold;'>♻️ Enter the value to convert</p>", unsafe_allow_html=True)
value = st.number_input("", min_value=0.01, step=0.01, key="value")


# Conversion Function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24
    return None


# Convert Button
if st.button("Convert"):
    if value > 0:
        result = convert_units(category, value, unit)
        if result is not None:
            st.success(f"The result is: **{result:.2f}**", icon="✅")
        else:
            st.warning("Invalid conversion. Please try again.")
    else:
        st.warning("Please enter a valid value.")

# Footer
st.markdown("<p style='text-align: center; font-size: 14px; color: white;'>Made with ❤️ by Jasmine Sheikh</p>", unsafe_allow_html=True)
