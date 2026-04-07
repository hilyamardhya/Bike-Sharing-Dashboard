import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)



# =========================
# LOAD DATA
# =========================
BASE_DIR = os.path.dirname(__file__)

day_path = os.path.join(BASE_DIR, "day.csv")
hour_path = os.path.join(BASE_DIR, "hour.csv")

day_df = pd.read_csv(day_path)
hour_df = pd.read_csv(hour_path)

# =========================
# PREPROCESSING
# =========================
day_df["dteday"] = pd.to_datetime(day_df["dteday"])

# =========================
# TITLE
# =========================
st.title("🚲 Bike Sharing Dashboard ")
st.markdown("Analisis penyewaan sepeda berdasarkan waktu, cuaca, dan aktivitas pengguna")

# =========================
# SIDEBAR FILTER
# =========================
st.sidebar.header("🔍 Filter Data")
dataset_choice = st.sidebar.radio(
    "Pilih Dataset",
    ["Harian", "Per Jam"]
)

# =========================
# FILTER TANGGAL (WAJIB)
# =========================
start_date = st.sidebar.date_input(
    "Tanggal Mulai",
    value=day_df["dteday"].min().date()
)

end_date = st.sidebar.date_input(
    "Tanggal Akhir",
    value=day_df["dteday"].max().date()
)

filtered_day = day_df[
    (day_df["dteday"] >= pd.to_datetime(start_date)) &
    (day_df["dteday"] <= pd.to_datetime(end_date))
]

# =========================
# DATA SELECTION
# =========================
if dataset_choice == "Harian":
    df = filtered_day.copy()

    season = st.sidebar.selectbox(
        "Pilih Musim",
        sorted(df["season"].unique())
    )
    df = df[df["season"] == season]

else:
    df = hour_df.copy()

    hour_range = st.sidebar.slider(
        "Rentang Jam",
        0, 23, (6, 18)
    )
    df = df[(df["hr"] >= hour_range[0]) & (df["hr"] <= hour_range[1])]

# =========================
# HANDLE DATA KOSONG
# =========================
if df.empty:
    st.warning("Data kosong, silakan ubah filter.")
    st.stop()

# =========================
# METRICS
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("Total Penyewaan", int(df["cnt"].sum()))
col2.metric("Rata-rata Penyewaan", int(df["cnt"].mean()))
col3.metric("Max Penyewaan", int(df["cnt"].max()))

st.markdown("---")

# =========================
# VISUALISASI UTAMA
# =========================
col1, col2 = st.columns(2)

# 📊 Pertanyaan 1
with col1:
    st.subheader("Perbedaan Rata-rata Penyewaan Sepeda Berdasarkan Cuaca (2011–2012)")
    fig, ax = plt.subplots()
    sns.barplot(x="weathersit", y="cnt", data=df, ax=ax)
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Rata-rata Penyewaan")
    st.pyplot(fig)

    st.caption("Cuaca cerah menghasilkan rata-rata penyewaan tertinggi dibanding kondisi lainnya.")

# 📊 Pertanyaan 2
with col2:
    if "workingday" in df.columns:
        st.subheader("Perbandingan Rata-rata Penyewaan Sepeda antara Hari Kerja dan Libur (2011–2012)")
        fig, ax = plt.subplots()
        sns.barplot(x="workingday", y="cnt", data=df, ax=ax)
        ax.set_xlabel("Working Day (1=Hari Kerja, 0=Hari Libur)")
        ax.set_ylabel("Rata-rata Penyewaan")
        st.pyplot(fig)

        st.caption("Hari kerja menunjukkan pola penyewaan yang lebih stabil dibandingkan hari libur.")

# =========================
# TAMBAHAN (HOUR)
# =========================
if dataset_choice == "Per Jam":
    st.subheader("Pola Penyewaan Sepeda per Jam")
    fig, ax = plt.subplots()
    sns.lineplot(x="hr", y="cnt", data=df, ax=ax)
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

# =========================
# DISTRIBUSI
# =========================
st.subheader("Distribusi Penyewaan Sepeda")

fig, ax = plt.subplots()
sns.histplot(df["cnt"], bins=30, kde=True, ax=ax)
ax.set_xlabel("Jumlah Penyewaan")
st.pyplot(fig)

# =========================
# INSIGHT
# =========================
st.markdown("### 💡 Insight")

st.info("""
- Cuaca cerah meningkatkan rata-rata penyewaan sepeda.
- Cuaca buruk menurunkan jumlah penyewaan secara signifikan.
- Hari kerja menunjukkan pola penyewaan yang lebih stabil dibandingkan hari libur.
- Filter tanggal memungkinkan analisis dinamis berdasarkan periode waktu tertentu.
""")