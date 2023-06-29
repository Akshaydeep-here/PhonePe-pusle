
import mysql.connector 
import pandas as pd
import streamlit as st
import PIL 
from PIL import Image
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import streamlit as st
import pandas as pd
# connect to the database
import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='Akshay@123', host='127.0.0.1', database="ph_db")

# create a cursor object
cursor = conn.cursor()

#with st.sidebar:
SELECT = option_menu(
    menu_title = None,
    options = ["About","Home","Basic insights","Contact"],
    icons =["bar-chart","house","toggles","at"],
    default_index=2,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "white","size":"cover", "width": "100%"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
        "nav-link-selected": {"background-color": "#6F36AD"}})


#---------------------Basic Insights -----------------#


if SELECT == "Basic insights":
    st.title("BASIC INSIGHTS")
    st.write("----")
    st.subheader("Let's know some basic insights about the data")
    options = ["--select--",
               "Top 10 states based on year and amount of transaction",
               "List 10 states based on type and amount of transaction",
               "Top 5 Transaction_Type based on Transaction_Amount",
               "Top 10 Registered-users based on States and District",
               "Top 10 Districts based on states and Count of transaction",
               "List 10 Districts based on states and amount of transaction",
               "List 10 Transaction_Count based on Districts and states",
               "Top 10 RegisteredUsers based on states and District"]
    
               #1
               
    select = st.selectbox("Select the option",options)
    if select=="Top 10 states based on year and amount of transaction":
        cursor.execute("SELECT DISTINCT States, Transaction_Year, SUM(Transaction_Amount) AS Total_Transaction_Amount FROM ph_db.top_tran GROUP BY States, Transaction_Year ORDER BY Total_Transaction_Amount DESC LIMIT 10");
        
        df = pd.DataFrame(cursor.fetchall(), columns=['States','Transaction_Year', 'Transaction_Amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 states and amount of transaction")
            st.bar_chart(data=df,x="Transaction_Amount",y="States")
            
            #2
            
    elif select=="List 10 states based on type and amount of transaction":
        cursor.execute("SELECT DISTINCT States, SUM(Transaction_Count) as Total FROM ph_db.top_tran GROUP BY States ORDER BY Total ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['States','Total_Transaction'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("List 10 states based on type and amount of transaction")
            st.bar_chart(data=df,x="Total_Transaction",y="States")
            
            #3
            
    elif select=="Top 5 Transaction_Type based on Transaction_Amount":
        cursor.execute("SELECT DISTINCT Transaction_Type, SUM(Transaction_Amount) AS Amount FROM ph_db.agg_user GROUP BY Transaction_Type ORDER BY Amount DESC LIMIT 5");
        df = pd.DataFrame(cursor.fetchall(),columns=['Transaction_Type','Transaction_Amount '])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 5 Transaction_Type based on Transaction_Amount")
            st.bar_chart(data=df,x="Transaction_Type",y="Amount")
            
            #4
            
    elif select=="Top 10 Registered-users based on States and District":
        cursor.execute("SELECT DISTINCT State, District, SUM(RegisteredUsers) AS Users FROM ph_db.top_user GROUP BY State, District ORDER BY Users DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','RegisteredUsers'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Registered-users based on States and District")
            st.bar_chart(data=df,x="State",y="RegisteredUsers")
            
            #5
            
    elif select=="Top 10 Districts based on states and Count of transaction":
        cursor.execute("SELECT DISTINCT States,District,SUM(Transaction_Count) AS Counts FROM ph_db.map_tran GROUP BY States,District ORDER BY Counts DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['States','District','Transaction_Count'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Districts based on states and Count of transaction")
            st.bar_chart(data=df,x="States",y="Transaction_Count")
            
            #6
            
    elif select=="List 10 Districts based on states and amount of transaction":
        cursor.execute("SELECT DISTINCT States,Transaction_year,SUM(Transaction_Amount) AS Amount FROM ph_db.agg_trans GROUP BY States, Transaction_year ORDER BY Amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['States','Transaction_year','Transaction_Amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Least 10 Districts based on states and amount of transaction")
            st.bar_chart(data=df,x="States",y="Transaction_Amount")
            
            #7
            
    elif select=="List 10 Transaction_Count based on Districts and states":
        cursor.execute("SELECT DISTINCT States, District, SUM(Transaction_Count) AS Counts FROM ph_db.map_tran GROUP BY States,District ORDER BY Counts ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['States','District','Transaction_Count'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("List 10 Transaction_Count based on Districts and states")
            st.bar_chart(data=df,x="States",y="Transaction_Count")
            
            #8
             
    elif select=="Top 10 RegisteredUsers based on states and District":
        cursor.execute("SELECT DISTINCT States,District, SUM(RegisteredUsers) AS Users FROM ph_db.map_user GROUP BY States,District ORDER BY Users DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns = ['States','District','RegisteredUsers'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 RegisteredUsers based on states and District")
            st.bar_chart(data=df,x="States",y="RegisteredUsers")


#----------------Home----------------------#

cursor = conn.cursor()

# execute a SELECT statement
cursor.execute("SELECT * FROM ph_db.agg_trans")

# fetch all rows
rows = cursor.fetchall()

if SELECT == "Home":
    col1,col2, = st.columns(2)
    col1.image(Image.open(r"D:\Data Science\ppp\PhonePe_Logo.jpg"),width = 400)
    with col2:
        df = pd.DataFrame(rows, columns=['States', 'Transaction_Year', 'Quarters', 'Transaction_Type', 'Transaction_Count','Transaction_Amount'])
        fig = px.choropleth(df, locations="States", scope="asia", color="States", hover_name="States",
            title="Live Geo Visualization of India")
        st.plotly_chart(fig)





#----------------About-----------------------#

if SELECT == "About":
    col1,col2 = st.columns(2)
    with col1:
        st.title("THE BEAT OF PHONEPE")
        st.write("---")
        st.subheader("Phonepe became a leading digital payments company")
        st.image(Image.open(r"D:\Data Science\ppp\top.jpeg"),width = 400)
        with open(r"D:\Data Science\ppp\annual report.pdf","rb") as f:
            data = f.read()
    with col2:
        st.image(Image.open(r"D:\Data Science\ppp\PhonePe_Logo.jpg"),width = 500)
        st.write("---")
        st.subheader("The Indian digital payments story has truly captured the world's imagination."
                 " From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and states-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government."
                 " Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. "
                 "PhonePe Pulse is our way of giving back to the digital payments ecosystem.")
    st.write("---")


#----------------------Contact---------------#




if SELECT == "Contact":
    name = "Akshaydeep Dade"
    mail = (f'{"Mail :"}  {"akshaydeepdade7111@gmail.com"}')
    description = "An Aspiring DATA-SCIENTIST..!"
    social_media = {
        
        "GITHUB": "https://github.com/Akshaydeep-here",
        "LINKEDIN": "http://www.linkedin.com/in/akshaydeep-dade",
        "INSTAGRAM": "https://www.instagram.com/omkaraksh/",
        "Portfolio": "https://akshaydeepdade.blogspot.com/",
        "Kaggle": "https://www.kaggle.com/omkarm0542"}
    
    col2,col1, col3 = st.columns(3)
    col3.image(Image.open(r"D:\Data Science\ppp\picofme.png"), width=450)
    with col2:
        st.title('Phonepe Pulse data visualisation')
        st.write("The goal of this project is to extract data from the Phonepe pulse Github repository, transform and clean the data, insert it into a MySQL database, and create a live geo visualization dashboard using Streamlit and Plotly in Python. The dashboard will display the data in an interactive and visually appealing manner, with at least 10 different dropdown options for users to select different facts and figures to display. The solution must be secure, efficient, and user-friendly, providing valuable insights and information about the data in the Phonepe pulse Github repository.")
        st.write("---")
        st.subheader(mail)
    st.write("#")
    cols = st.columns(len(social_media))
    for index, (platform, link) in enumerate(social_media.items()):
        cols[index].write(f"[{platform}]({link})")



