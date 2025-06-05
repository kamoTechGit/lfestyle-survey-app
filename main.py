import streamlit as st
from database import init_db

# Initialize database
init_db()

# Page configuration
st.set_page_config(
    page_title="Lifestyle Survey",
    page_icon="📊",
    layout="wide"
)

# Custom sidebar navigation
st.sidebar.title("📋 Navigation")
st.sidebar.page_link("main.py", label="🏠 Home")
st.sidebar.page_link("pages/1_Fill_Survey.py", label="✍️ Fill Survey")
st.sidebar.page_link("pages/2_View_Results.py", label="📊 View Results")

# Hide default Streamlit menu
st.markdown("""
<style>
[data-testid="stSidebarNav"] { display: none; }
</style>
""", unsafe_allow_html=True)

# Homepage content
st.title("Welcome to the Lifestyle Survey!")
st.markdown("""
Use this app to:
- Submit your lifestyle preferences
- View aggregated survey results

Navigate using the sidebar menu.
""")