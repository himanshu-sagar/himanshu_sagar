import streamlit as st
import pandas as pd

st.set_page_config(page_title='Himanshu Sagar\'s portfolio', page_icon='👨‍🔬')
# Start App
st.title("Hey! I'm Himanshu Sagar🧑🏽")

st.write(
    """
    I'm data driven computer science engineer🧑🏽‍💻, 
    passionate about machine learning, 
    experienced in building AI powered right career prediction model,
    looking for job opportunity where I 
can use my experience and skills to 
help our society.
    """
)

########## Education ##########
st.header("Education 📖")

education = [
    {"Education": "Bachelor of Technology (CSE)", "Org": "Lovely Professional University", "Year": "2022"},
    {"Education": "Senior Secondary Education", "Org": "R.J.S Inter College", "Year": "2018"},
    {"Education": "Secondary Education", "Org": "Doon Senior Secondary School", "Year": "2015"},
]
ed_df = pd.DataFrame(education)
st.table(ed_df)

########## Skills ##########
st.header("Skills 💪")
skills = ["Python", "Pandas", "Streamlit", "Machine Learning", "Data Science", "Data Visualization", "Data Analysis"]
c1, c2, c3, c4 = st.columns(4)
for i in range(len(skills)):
    if i % 4 == 0:
        c1.markdown("***" + skills[i] + "***" )
    elif i % 4 == 1:
        c2.markdown("***" + skills[i] + "***" )
    elif i % 4 == 2:
        c3.markdown("***" + skills[i] + "***" )
    else:
        c4.markdown("***" + skills[i] + "***" )