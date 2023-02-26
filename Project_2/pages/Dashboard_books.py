import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

#absolute path to this file
 
FILE_DIR = os.path.dirname(os.path.abspath(__file__))

#absolute path to this file's root directory

PARENT_DIR = os.path.join(FILE_DIR,os.pardir)

#absolute path of directory_of_intrest

dir_of_intrest = os.path.join(PARENT_DIR,"resources")

IMAGE_PATH = os.path.join(dir_of_intrest,"images","image.jpg")
DATA_PATH = os.path.join(dir_of_intrest,"data","IMDb_All_Genres_etf_clean1.csv")

st.title("Dashboard - IMDb_All_Genres_etf_clean1 Data")

img =image.imread(IMAGE_PATH)
st.image(img)
df = pd.read_csv(DATA_PATH,encoding='utf-8')

col1,col2=st.columns(2)
fig_1=px.histogram(df['Rating'])
col1.plotly_chart(fig_1,use_container_width=True)
fig_2=px.scatter(df,x='main_genre',y='Rating')
col2.plotly_chart(fig_2,use_container_width=True)