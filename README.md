# 🚲 Dashboard Analisis Bike Sharing

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis faktor-faktor yang memengaruhi jumlah penyewaan sepeda menggunakan Bike Sharing Dataset. Analisis dilakukan melalui beberapa tahapan, yaitu data wrangling, exploratory data analysis (EDA), visualisasi data, hingga pembuatan dashboard interaktif menggunakan Streamlit.

Dataset yang digunakan berisi informasi terkait kondisi cuaca, musim, hari kerja, serta jumlah penyewaan sepeda baik oleh pengguna terdaftar maupun pengguna kasual.

---

## 🎯 Pertanyaan Bisnis

1. Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?
2. Apakah terdapat perbedaan jumlah penyewaan sepeda antara hari kerja dan hari libur?

---

## 🧹 Tahapan Analisis Data

### 1. Data Wrangling

Tahap ini dilakukan untuk mempersiapkan data sebelum dianalisis. Kegiatan yang dilakukan meliputi:

* Mengimpor dataset
* Memeriksa struktur data
* Mengidentifikasi missing value
* Melakukan transformasi tipe data

**Hasil:**
Data dalam kondisi bersih dan siap digunakan untuk analisis lebih lanjut.

---

### 2. Exploratory Data Analysis (EDA)

Tahap ini bertujuan untuk memahami pola dan karakteristik data.

**Analisis yang dilakukan:**

* Menghitung rata-rata jumlah penyewaan berdasarkan kondisi cuaca
* Membandingkan jumlah penyewaan antara hari kerja dan hari libur

**Hasil:**
Ditemukan bahwa faktor seperti cuaca dan hari kerja memiliki pengaruh terhadap jumlah penyewaan sepeda.

---

### 3. Visualisasi Data

Visualisasi digunakan untuk memperjelas hasil analisis.

**Visualisasi yang dibuat:**

* Grafik pengaruh cuaca terhadap penyewaan sepeda
* Grafik perbandingan hari kerja dan hari libur

**Hasil:**
Cuaca cerah meningkatkan jumlah penyewaan, sedangkan cuaca buruk menurunkannya.

---

### 4. Analisis Lanjutan (Clustering/Binning)

Dilakukan pengelompokan jumlah penyewaan menjadi kategori:

* Rendah
* Sedang
* Tinggi

**Tujuan:**
Mengetahui distribusi penggunaan sepeda secara lebih terstruktur.

**Hasil:**
Sebagian besar data berada pada kategori sedang, menunjukkan penggunaan sepeda yang relatif stabil.

---

## 📊 Insight Utama

* Kondisi cuaca memiliki pengaruh signifikan terhadap jumlah penyewaan sepeda
* Penyewaan meningkat pada cuaca cerah
* Hari kerja memiliki pola penyewaan yang lebih stabil dibandingkan hari libur
* Sebagian besar penyewaan berada dalam kategori sedang

---

## 🧾 Kesimpulan

### 🔹 Pertanyaan 1

Kondisi cuaca berpengaruh signifikan terhadap jumlah penyewaan sepeda. Cuaca cerah meningkatkan aktivitas penyewaan, sedangkan kondisi cuaca buruk seperti hujan menurunkan jumlah penyewaan.

### 🔹 Pertanyaan 2

Terdapat perbedaan pola penyewaan antara hari kerja dan hari libur. Hari kerja cenderung memiliki pola penyewaan yang lebih stabil dibandingkan hari libur yang lebih fluktuatif.

---

## 💻 Cara Menjalankan Dashboard

Buka link berikut di browser:
https://bike-sharing-dashboard-hjopvpsdu4p6ra6fzrm25r.streamlit.app/

---

## 📁 Struktur Folder

```
submission/
│
├── dashboard/
│   ├── app.py
│   ├── day.csv
│   └── hour.csv
│
├── data/
│   ├── day.csv
│   ├── hour.csv
│   └── README.txt
│
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

---

## 👤 Author

Nama: Hilya Mardhya
Email: [hmardhya@gmail.com](mailto:hmardhya@gmail.com)
