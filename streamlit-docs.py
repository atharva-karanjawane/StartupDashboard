import pandas as pd
import streamlit as st
import time

# Streamlit Docs -------------> https://docs.streamlit.io

# Write Commands --------
st.title('Startup Dashboard')
st.header('I am learning Streamlit')
st.subheader('And i am loving it')
st.write("Try and run it through the command prompt (anaconda prompt). If it tells you that streamlit command cannot be recognised and you are sure you have installed streamlit to your environment, then add Anaconda folder into your Windows path. To do this, go to Advanced")

# Markdown ------------
st.markdown(
    """
        ### Top 5 Colleges in Pune:
        - COEP
        - PICT
        - VIT
        - Cummins
        - PCCOE
    """
)
# Code Block ------------
st.code("""
    # 1. pd.MultiIndex.from_tuples()
    index_val = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
    multiindex = pd.MultiIndex.from_tuples(index_val)
    multiindex.levels[1]

    # 2. pd.MultiIndex.from_product()
    pd.MultiIndex.from_product([['cse','ece'],[2019,2020,2021,2022]])
    """
)

# LaTeX Commands ------------
st.latex("""
    x^2 + y^2 = a^2
""")

# Display Commands -------------------

df = pd.DataFrame(
    {
        "Name":["Atharva","Parth","Vedant","Rohan","Gautami"],
        "Branch":['AIDS','AIDS','AIDS','Electrical','EXTC'],
        "CGPA":[9.86,9.00,8.86,7.86,9.50]
    }
)
avg_cgpa = df['CGPA'].mean()
# Displaying Dataframes ----------------
st.dataframe(df)

# Displaying Metrics -------------------
st.metric('Avg CGPA',avg_cgpa,"+12%")

# Displaying JSON --------------------
st.json(
    {
        "Name":["Atharva","Parth","Vedant","Rohan","Gautami"],
        "Branch":['AIDS','AIDS','AIDS','Electrical','EXTC'],
        "CGPA":[9.86,9.00,8.86,7.86,9.50]
    }
)

# Displaying Media ------------------

st.image('athu_photo.png',caption="Atharva Karanjawane")
st.video('Habbinson Video Internship.mp4')
st.audio('(Audio) LMS_1.m4a')

# Sidebar --------------
st.sidebar.title('Table of Content')


# in row display ------------------
col1,col2 = st.columns(2)
with col1:
    st.image('athu_photo.png', caption="Atharva Karanjawane")

with col2:
    st.image('atharva photo (1).jpg', caption="Atharva Karanjawane")

# Messages ------------------------
st.error("Login Failed")
st.success("Login Succesful")
st.info("Enter in CAPS")
st.warning("Keep your PassKey Safe")

# Progress Bar ---------------------
bar = st.progress(0)
for i in range (100):
    time.sleep(0.1)
    bar.progress(i)

# User Input -----------------------
email = st.text_input("Enter Email")
password = st.text_input('Enter Password')
age = st.number_input('Enter Age')
dob = st.date_input('Enter DOB')

# Buttons -------------------------
btn = st.button("Login")
if btn:
    if email == "athuhero@gmail.com" and password == "athuhero":
        st.success('Login Succesful')
        st.balloons()
    else:
        st.error('Password or email is incorrect')

# DropDown --------------------------
gender = st.selectbox("Select Your Gender",['Male','Female','Others'])

# File Upload ------------------------
user_file = st.file_uploader('Upload a csv file')
if user_file is not None:
    df = pd.read_csv(user_file)
    st.dataframe(df.describe())
