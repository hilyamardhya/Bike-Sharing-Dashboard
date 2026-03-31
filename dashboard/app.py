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
# LOAD DATA (ANTI ERROR CLOUD)
# =========================
BASE_DIR = os.path.dirname(__file__)

day_path = os.path.join(BASE_DIR, "day.csv")
hour_path = os.path.join(BASE_DIR, "hour.csv")

day_df = pd.read_csv(day_path)
hour_df = pd.read_csv(hour_path)

# =========================
# STYLE
# =========================
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
h1 {
    color: #2c3e50;
}
</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.title("🚲 Bike Sharing Dashboard")
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
# DATA SELECTION
# =========================
if dataset_choice == "Harian":
    df = day_df.copy()
    
    season = st.sidebar.selectbox("Pilih Musim", sorted(df["season"].unique()))
    df = df[df["season"] == season]

else:
    df = hour_df.copy()
    
    hour_range = st.sidebar.slider("Rentang Jam", 0, 23, (6, 18))
    df = df[(df["hr"] >= hour_range[0]) & (df["hr"] <= hour_range[1])]

# =========================
# HANDLE DATA KOSONG (ANTI ERROR)
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

# Grafik 1 - Cuaca
with col1:
    st.subheader("🌦️ Cuaca vs Penyewaan")
    fig, ax = plt.subplots()
    sns.barplot(x="weathersit", y="cnt", data=df, ax=ax)
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

# Grafik 2 - Working Day
with col2:
    if "workingday" in df.columns:
        st.subheader("📅 Hari Kerja vs Libur")
        fig, ax = plt.subplots()
        sns.barplot(x="workingday", y="cnt", data=df, ax=ax)
        ax.set_xlabel("Working Day (1=Ya, 0=Tidak)")
        ax.set_ylabel("Jumlah Penyewaan")
        st.pyplot(fig)

# =========================
# GRAFIK TAMBAHAN (HOUR)
# =========================
if dataset_choice == "Per Jam":
    st.subheader("⏰ Pola Penyewaan per Jam")
    fig, ax = plt.subplots()
    sns.lineplot(x="hr", y="cnt", data=df, ax=ax)
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

# =========================
# DISTRIBUSI
# =========================
st.subheader("📊 Distribusi Penyewaan")

fig, ax = plt.subplots()
sns.histplot(df["cnt"], bins=30, kde=True, ax=ax)
ax.set_xlabel("Jumlah Penyewaan")
st.pyplot(fig)

# =========================
# INSIGHT
# =========================
st.markdown("### 💡 Insight")

st.info("""
- Cuaca memiliki pengaruh signifikan terhadap jumlah penyewaan sepeda.
- Penyewaan meningkat pada kondisi cuaca cerah.
- Aktivitas tertinggi terjadi pada jam sibuk (pagi dan sore hari).
- Hari kerja menunjukkan pola penggunaan yang lebih stabil dibandingkan hari libur.
""")