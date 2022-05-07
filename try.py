import streamlit as st
import plotly_express as px
import pandas as pd

st.set_page_config(page_title="HR salary prediction Dashboard", layout="wide")


df=pd.read_csv('data.csv')


global numeric_columns
global non_numeric_columns
try:
    st.write(df)
    numeric_columns = list(df.select_dtypes(['float', 'int64']).columns)
    non_numeric_columns = list(df.select_dtypes(['object']).columns)
    non_numeric_columns.append(None)
    print(non_numeric_columns)
except Exception as e:
    print(e)
    st.write("Please upload file to the application.")

# add a select widget to the side bar
chart_select = st.sidebar.selectbox(
    label="Select the chart type",
    options=['Histogram','Histogram1']
)
if chart_select == 'Histogram':
    st.sidebar.subheader("Histogram Settings")
    try:
        x = st.sidebar.selectbox('Feature', options=numeric_columns)
        bin_size = st.sidebar.slider("Number of Bins", min_value=10,
                                     max_value=100, value=40)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.histogram(x=x, data_frame=df, color=color_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
if chart_select == 'Histogram1':
    st.sidebar.subheader("Histogram Settings")
    try:
        x = st.sidebar.selectbox('Feature', options=non_numeric_columns)
        bin_size = st.sidebar.slider("Number of Bins", min_value=10,
                                     max_value=100, value=40)
        color_value = st.sidebar.selectbox("Color", options=numeric_columns)
        plot = px.histogram(x=x, data_frame=df, color=color_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Boxplot':
    st.sidebar.subheader("Boxplot Settings")
    try:
        y = st.sidebar.selectbox("Y axis", options=numeric_columns)
        x = st.sidebar.selectbox("X axis", options=non_numeric_columns)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.box(data_frame=df, y=y, x=x, color=color_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
