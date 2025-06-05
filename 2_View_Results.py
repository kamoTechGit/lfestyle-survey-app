import streamlit as st
from database import get_survey_stats

st.title("📊 Survey Results")

stats = get_survey_stats()

if stats.get('total', 0) == 0:
    st.warning("No surveys available yet. Please submit some data!")
    st.stop()

# Display results in two columns
col1, col2 = st.columns(2)

with col1:
    st.metric("Total surveys", stats['total'])
    st.metric("Average age", f"{stats['avg_age']:.1f} years")
    st.metric("Oldest participant", f"{stats['max_age']:.1f} years")
    st.metric("Youngest participant", f"{stats['min_age']:.1f} years")

with col2:
    st.metric("Like Pizza", f"{(stats['pizza']/stats['total'])*100:.1f}%")
    st.metric("Like Pasta", f"{(stats['pasta']/stats['total'])*100:.1f}%")
    st.metric("Like Pap and Wors", f"{(stats['pap_wors']/stats['total'])*100:.1f}%")

st.subheader("Average Ratings (1=Strongly Agree, 5=Strongly Disagree)")
st.metric("I like to watch movies", f"{stats['movies']:.1f}")
st.metric("I like to listen to radio", f"{stats['radio']:.1f}")
st.metric("I like to eat out", f"{stats['eat_out']:.1f}")
st.metric("I like to watch TV", f"{stats['tv']:.1f}")