import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

def create_daily_users_df(df):
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df.groupby(
        pd.Grouper(key='dteday', freq='6MS')  # Group by 6-month periods
    ).agg({
        "registered_daily": "mean",
        "cnt_daily": "mean",
        "casual_daily": "mean"
    }).reset_index()

def create_hourly_users_df(df):
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df.groupby(
        pd.Grouper(key='dteday', freq='6MS')  # Group by 6-month periods
    ).agg({
        "registered_hourly": "mean",
        "cnt_hourly": "mean",
        "casual_hourly": "mean"
    }).reset_index()

def create_seasonal_daily_users_df(df):
    return df.groupby(by="season_daily").agg({
    "casual_daily": "sum",
    "registered_daily": "sum",
    "cnt_daily":  "sum"
}).reset_index()

def create_seasonal_hourly_users_df(df):
    return df.groupby(by="season_hourly").agg({
    "casual_hourly": "sum",
    "registered_hourly": "sum",
    "cnt_hourly":  "sum"
}).reset_index()

all_df = pd.read_csv('dashboard/main_data.csv')

daily_users_df = create_daily_users_df(all_df)
hourly_users_df = create_hourly_users_df(all_df)
seasonal_daily_users_df = create_seasonal_daily_users_df(all_df)
seasonal_hourly_users_df = create_seasonal_hourly_users_df(all_df)

st.header('Bike Sharing Collection Dashboard')
tab1, tab2 = st.tabs(["Users", "Season"])

with tab1:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(daily_users_df['dteday'], daily_users_df['registered_daily'], label='Registered Daily', marker='o',)
    ax.plot(daily_users_df['dteday'], daily_users_df['cnt_daily'], label='Total Daily', marker='o',)
    ax.plot(daily_users_df['dteday'], daily_users_df['casual_daily'], label='Casual Daily', marker='o',)

    ax.set_title('Average user type per 6 month daily in 2011 - 2012')
    ax.set_xlabel('Date')
    ax.set_ylabel('Users')
    ax.legend()

    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(hourly_users_df['dteday'], hourly_users_df['registered_hourly'], label='Registered Hourly', marker='o',)
    ax.plot(hourly_users_df['dteday'], hourly_users_df['cnt_hourly'], label='Total Hourly', marker='o',)
    ax.plot(hourly_users_df['dteday'], hourly_users_df['casual_hourly'], label='Casual Hourly', marker='o',)

    ax.set_title('Average user type per 6 month hourly in 2011 - 2012')
    ax.set_xlabel('Date')
    ax.set_ylabel('Users')
    ax.legend()

    st.pyplot(fig)

with tab2:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(seasonal_daily_users_df['season_daily'], seasonal_daily_users_df['cnt_daily'], color='skyblue', label='Casual Daily Users')

    ax.set_title('Total user per season daily in 2011 - 2012')
    ax.set_xlabel('Date')
    ax.set_ylabel('Users')
    ax.legend()

    plt.xticks(rotation=45)

    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(seasonal_hourly_users_df['season_hourly'], seasonal_hourly_users_df['cnt_hourly'], color='skyblue', label='Casual Hourly Users')

    ax.set_title('Total user per season hourly in 2011 - 2012')
    ax.set_xlabel('Date')
    ax.set_ylabel('Users')
    ax.legend()

    plt.xticks(rotation=45)

    st.pyplot(fig)