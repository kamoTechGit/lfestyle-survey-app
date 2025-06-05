import streamlit as st
from datetime import date
from database import save_survey

st.title("📝 Lifestyle Preferences Survey")

with st.form("survey_form"):
    # Personal Details
    st.subheader("Personal Details")
    full_name = st.text_input("Full Name*")
    email = st.text_input("Email*")
    dob = st.date_input("Date of Birth*", min_value=date(1900, 1, 1), max_value=date.today())
    contact = st.text_input("Contact Number*")
    
    # Favorite Food
    st.subheader("What is your favorite food? (Select all that apply)")
    pizza = st.checkbox("Pizza")
    pasta = st.checkbox("Pasta")
    pap_wors = st.checkbox("Pap and Wors")
    other_food = st.text_input("Other (please specify)")
    
    # Rating Questions
    st.subheader("Please rate your level of agreement (1=Strongly Agree, 5=Strongly Disagree)")
    movies = st.radio("I like to watch movies", [1, 2, 3, 4, 5], horizontal=True, index=None)
    radio = st.radio("I like to listen to radio", [1, 2, 3, 4, 5], horizontal=True, index=None)
    eat_out = st.radio("I like to eat out", [1, 2, 3, 4, 5], horizontal=True, index=None)
    tv = st.radio("I like to watch TV", [1, 2, 3, 4, 5], horizontal=True, index=None)
    
    submitted = st.form_submit_button("Submit Survey")
    
    if submitted:
        if not all([full_name, email, contact]):
            st.error("Please fill in all required fields (marked with *)")
        elif (date.today() - dob).days/365 < 5 or (date.today() - dob).days/365 > 120:
            st.error("Age must be between 5 and 120 years")
        elif None in [movies, radio, eat_out, tv]:
            st.error("Please provide ratings for all statements")
        else:
            save_survey(full_name, email, dob, contact, pizza, pasta, pap_wors, other_food, 
                       movies, radio, eat_out, tv)
            st.success("✅ Thank you for completing the survey!")