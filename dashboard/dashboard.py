import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def create_df_weather(df, selected_weathersit=None):
    if selected_weathersit is not None:
        df = df[df['weathersit'] == selected_weathersit]
    return df.groupby(['weathersit']).agg({
        'temp': 'mean',
        'atemp': 'mean',
        'hum': 'mean',
        'windspeed': 'mean'
    }).reset_index()


def create_df_year(df, selected_year=None):
    if selected_year is not None:
        df = df[df['yr'] == selected_year]
    return df.groupby(by='yr').agg({
        'casual': 'sum',
        'registered': 'sum',
        'cnt': 'sum'
    }).reset_index()

day_df = pd.read_csv('data/day.csv')

st.title("Bike Sharing Data Analysis")

weathersit_options = day_df['weathersit'].unique()
selected_weathersit = st.selectbox(
    "Select Weather Situation",
    options=[None] + list(weathersit_options),
    format_func=lambda x: "All" if x is None else f"Weather Situation {x}"
)

day_df_weather = create_df_weather(day_df, selected_weathersit)

st.header("Average Environment Condition Metrics by Weather Situation")

if not day_df_weather.empty:
    fig, ax = plt.subplots(figsize=(10, 6))
    day_df_weather.plot(kind='bar', x='weathersit', y=['temp', 'atemp', 'hum', 'windspeed'], ax=ax)
    ax.set_ylabel('Average Value')
    ax.set_xlabel('Weather Situation')
    plt.xticks(rotation=0)
    st.pyplot(fig)
else:
    st.write("No data available for the selected weather situation.")

year_options = day_df['yr'].unique()
selected_year = st.selectbox(
    "Select Year",
    options=[None] + list(year_options),
    format_func=lambda x: "All" if x is None else f"Year {x + 1}"
)

day_df_year = create_df_year(day_df, selected_year)

st.header("Total Type User Count by Year")
if not day_df_year.empty:
    day_df_year['yr'] = day_df_year['yr'] + 1 
    fig, ax = plt.subplots(figsize=(10, 6))
    day_df_year.plot(kind='bar', x='yr', y=['cnt', 'registered', 'casual'], ax=ax, stacked=True)
    ax.set_ylabel('Total User Count')
    ax.set_xlabel('Year')
    plt.xticks(rotation=0)
    st.pyplot(fig)
else:
    st.write("No data available for the selected year.")

