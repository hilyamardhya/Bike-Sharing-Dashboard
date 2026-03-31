import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

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
# SIDEBAR
# =========================
st.sidebar.header("🔍 Filter")

dataset_choice = st.sidebar.radio(
    "Pilih Dataset",
    ["Harian", "Per Jam"]
)

# =========================
# DATA SELECTION
# =========================
if dataset_choice == "Harian":
    df = day_df
    season = st.sidebar.selectbox("Musim", df["season"].unique())
    df = df[df["season"] == season]

else:
    df = hour_df
    hour_range = st.sidebar.slider("Rentang Jam", 0, 23, (6, 18))
    df = df[(df["hr"] >= hour_range[0]) & (df["hr"] <= hour_range[1])]

# =========================
# METRICS
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("Total Penyewaan", int(df["cnt"].sum()))
col2.metric("Rata-rata Penyewaan", int(df["cnt"].mean()))
col3.metric("Max Penyewaan", int(df["cnt"].max()))

st.markdown("---")

# =========================
# VISUALISASI
# =========================
col1, col2 = st.columns(2)

# Grafik 1
with col1:
    st.subheader("🌦️ Cuaca vs Penyewaan")
    fig, ax = plt.subplots()
    sns.barplot(x="weathersit", y="cnt", data=df, ax=ax)
    st.pyplot(fig)

# Grafik 2
with col2:
    st.subheader("📅 Hari Kerja vs Libur")
    if "workingday" in df.columns:
        fig, ax = plt.subplots()
        sns.barplot(x="workingday", y="cnt", data=df, ax=ax)
        st.pyplot(fig)

# =========================
# GRAFIK TAMBAHAN
# =========================
if dataset_choice == "Per Jam":
    st.subheader("⏰ Pola Penyewaan per Jam")

    fig, ax = plt.subplots()
    sns.lineplot(x="hr", y="cnt", data=df, ax=ax)
    st.pyplot(fig)

# =========================
# DISTRIBUSI
# =========================
st.subheader("📊 Distribusi Penyewaan")

fig, ax = plt.subplots()
sns.histplot(df["cnt"], bins=30, kde=True, ax=ax)
st.pyplot(fig)

# =========================
# INSIGHT BOX
# =========================
st.markdown("### 💡 Insight")
st.info("""
- Cuaca cerah meningkatkan jumlah penyewaan sepeda.
- Aktivitas tertinggi terjadi pada jam sibuk (pagi & sore).
- Hari kerja menunjukkan pola penggunaan yang lebih stabil.
- Sebagian besar penyewaan berada pada kategori menengah.
""")