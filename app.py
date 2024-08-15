import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='Startup Analysis')
def load_investors_details(investor):
    st.title(investor)

    # load recent 5 investments
    last5 = df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader("Most Recent Investments")
    st.dataframe(last5)

    # Biggest Investment
    col1,col2 = st.columns(2)
    with col1:
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader("Biggest Investments")
        #st.dataframe(big_series)

        # Plotting a bar graph
        fig,ax = plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)

    with col2:
        vert_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors Invested in')
        fig, ax = plt.subplots()
        ax.pie(vert_series,labels=vert_series.index,autopct="%0.01f%%")
        st.pyplot(fig)


df = pd.read_csv('startup_cleaned.csv')
st.sidebar.title("Startup Funding Analysis")

option = st.sidebar.selectbox("Select One",['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
    st.title("Overall Analysis")
elif option == "Startup":
    st.sidebar.selectbox("Select Startup",sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button("Find Startup Details")
else:
    selected_investor = st.sidebar.selectbox("Select Investor",sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button("Find Investor Details")
    if btn2:
        load_investors_details(selected_investor)
