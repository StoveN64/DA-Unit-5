
import streamlit as st
import pandas as pd
import numpy as np

st.title('Supermarket Data')

df = pd.read_csv('supermarket.csv')


st.subheader('Top 5 Daily Customer Count')

df_top_5_daily_customer_count = df.sort_values('daily_customer_count', ascending=False)

st.bar_chart(df_top_5_daily_customer_count.daily_customer_count.head())

st.subheader('Top 5 Sales Per customer')

df['spc'] = df.store_sales / df.daily_customer_count

df_top_5_sales_per_customer = df.sort_values('spc', ascending=False)

st.bar_chart(df_top_5_sales_per_customer.spc.head())

st.subheader('Top 5 Stores')

df_top_5_sellers = df.sort_values('store_sales', ascending=False)

st.bar_chart(df_top_5_sellers.store_sales.head())