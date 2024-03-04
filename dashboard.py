import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

#Menyiapkan dataFrame
def create_sum_yr_df(df):
    df["yr_text"] = df["yr"].replace({
        0: "2011",
        1: "2012"
    })
    sum_yr_df = df.groupby(by="yr_text").cnt.sum().sort_values(ascending=False)
    return sum_yr_df

def create_sum_season_df(df):
    df["season_text"] = df["season"].replace({
        1: "Springer", 
        2: "Summer", 
        3: "Fall", 
        4: "Winter"
    })
    sum_season_df = df.groupby(by="season_text").cnt.sum().sort_values(ascending=False)
    return sum_season_df

def create_sum_weather_df(df):
    df["weathersit_text"] = df["weathersit"].replace({
        1: "Cerah",
        2: "Kabut",
        3: "Salju Ringan",
        4: "Hujan Lebat"
    })
    sum_weather_df = df.groupby(by="weathersit_text").cnt.sum().sort_values(ascending=False)
    return sum_weather_df

#Load data
all_df = pd.read_csv("dashboard\main_df.csv")
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://allvectorlogo.com/img/2017/07/cogo-bike-share-logo.png")
    # Memilih opsi visualisasi
    option = st.sidebar.selectbox("Pilih Visualisasi Data", ["Year", "Season", "Weather"])

# Memanggil helper function yg sudah dibuat tadi
sum_yr_df = create_sum_yr_df(all_df)
sum_season_df = create_sum_season_df(all_df)
sum_weather_df = create_sum_weather_df(all_df)

#Melengkapi dashboard dengan berbagai visualisasi data
st.header('COGO Bike Share Dashboard :sparkles:')

if option == 'Year':
    # Menampilkan jumlah sewa sepeda untuk setiap tahun
    st.subheader("Tren jumlah penyewaan sepeda dari tahun 2011 ke tahun 2012")
    st.metric(label="Jumlah Penyewa Tertinggi", value="2.05 juta", delta="2012")
    fig, ax = plt.subplots(figsize=(20, 10))
    colors = ["#90CAF9", "#D3D3D3"]

    sns.barplot(
        y=sum_yr_df.values, 
        x=sum_yr_df.index,
        palette=colors,
        ax=ax
    )
    ax.set_title("Jumlah Penyewa Sepeda dari Tahun 2011 ke 2012", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)
    # Menampilkan dataframe
    st.dataframe(data=sum_yr_df, width=500, height=150)

elif option == 'Season':
    # Menampilkan jumlah sewa sepeda untuk setiap jenis musim
    st.subheader("Pengaruh Musim terhadap Jumlah Penyewa Sepeda")
    st.metric(label="Jumlah Penyewa Tertinggi", value="1.06 juta", delta="Fall")
    fig, ax = plt.subplots(figsize=(20, 10))
    colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(
        y=sum_season_df.values, 
        x=sum_season_df.index,
        palette=colors,
        ax=ax
    )
    ax.set_title("Jumlah Penyewa Sepeda berdasarkan Jenis Musim", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)
    # Menampilkan dataframe
    st.dataframe(data=sum_season_df, width=500, height=150)


elif option == 'Weather':
    # Menampilkan jumlah sewa sepeda untuk setiap jenis cuaca
    st.subheader("Pengaruh Cuaca terhadap Jumlah Penyewa Sepeda")
    st.metric(label="Jumlah Penyewa Tertinggi", value="2.26 juta", delta="Cuaca Cerah")
    fig, ax = plt.subplots(figsize=(20, 10))
    colors = ["#90CAF9", "#D3D3D3", "#D3D3D3"]

    sns.barplot(
        y=sum_weather_df.values, 
        x=sum_weather_df.index,
        palette=colors,
        ax=ax
    )
    ax.set_title("jumlah sewa sepeda untuk setiap jenis cuaca", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)
    # Menampilkan dataframe
    st.dataframe(data=sum_weather_df, width=500, height=150)

else:
    st.warning("Please select the available options")

st.caption('Copyright (c) COGO BikeShare 2024')