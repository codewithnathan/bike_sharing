import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def create_df_weather(df):
    return df.groupby(['weathersit']).agg({
        'temp': 'mean',
        'atemp': 'mean',
        'hum': 'mean',
        'windspeed': 'mean'
    }).reset_index()

def create_df_year(df):
    return df.groupby(by='yr').agg({
        'casual': 'sum',
        'registered': 'sum',
        'cnt': 'sum',
    }).reset_index()

day_df = pd.read_csv('data/day.csv')

day_df_weather = create_df_weather(day_df)
day_df_year = create_df_year(day_df)

st.title("Bike Sharing Data Analysis")

st.header("Average Environment Condition Metrics by Weather Situation")
fig, ax = plt.subplots(figsize=(10, 6))
day_df_weather.plot(kind='bar', x='weathersit', y=['temp', 'atemp', 'hum', 'windspeed'], ax=ax)
ax.set_ylabel('Average Value')
ax.set_xlabel('Weather Situation')
plt.xticks(rotation=0)
st.pyplot(fig)

st.header("Total Type User Count by Year")
fig, ax = plt.subplots(figsize=(10, 6))
day_df_year.plot(kind='bar', x='yr', y=['cnt', 'registered', 'casual'], ax=ax, stacked=True)
ax.set_ylabel('Total User Count')
ax.set_xlabel('Year')
plt.xticks(rotation=0)
st.pyplot(fig)
