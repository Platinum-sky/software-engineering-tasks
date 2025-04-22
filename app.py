import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("vehicles_us.csv")

# Header
st.header("Used Car Data Explorer")

# Checkbox to show/hide raw data
if st.checkbox("Show raw data"):
    st.write(df.head())

# Plotly histogram: Price distribution
st.subheader("Distribution of Car Prices")
fig_hist = px.histogram(df, x="price", nbins=50, title="Car Price Distribution")
st.plotly_chart(fig_hist)

# Plotly scatter: Price vs. Odometer
st.subheader("Price vs. Odometer")
fig_scatter = px.scatter(df, x="odometer", y="price", color="condition",
                         title="Car Price vs. Mileage by Condition")
st.plotly_chart(fig_scatter)