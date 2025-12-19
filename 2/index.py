import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Mengatur gaya visualisasi agar lebih rapi
sns.set_theme(style="whitegrid")

#Pada sel ini, kita melakukan import library pandas untuk pengolahan data, serta seaborn dan matplotlib untuk keperluan visualisasi grafik.

# Memuat dataset Titanic
df = sns.load_dataset('titanic')

# Menampilkan 5 baris pertama data
df.head()

#Kita memuat dataset Titanic ke dalam variabel df dan menampilkan 5 data teratas untuk melihat gambaran awal isi data.

# Melihat ringkasan informasi dataset
df.info()

#Fungsi .info() digunakan untuk memeriksa tipe data setiap kolom dan mengecek apakah ada nilai yang kosong (null).

# Melihat statistik dasar data numerik
df.describe()

#Fungsi .describe() menampilkan ringkasan statistik seperti rata-rata (mean), nilai minimum, dan maksimum dari data numerik.

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='alive', palette='pastel')
plt.title('Jumlah Penumpang Selamat vs Meninggal')
plt.show()

#Visualisasi ini membandingkan jumlah penumpang yang selamat dan yang tidak selamat menggunakan Bar Chart

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='age', kde=True, color='blue')
plt.title('Distribusi Umur Penumpang')
plt.show()

#Histogram ini menunjukkan penyebaran usia penumpang. Kurva KDE memperlihatkan kepadatan distribusi usia.

plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='class', y='survived', palette='viridis')
plt.title('Tingkat Keselamatan Berdasarkan Kelas Tiket')
plt.ylabel('Peluang Selamat (0-1)')
plt.show()

#Grafik ini memperlihatkan hubungan antara kelas tiket dengan peluang keselamatan. Penumpang kelas satu memiliki rata-rata selamat paling tinggi.

plt.figure(figsize=(8, 6))
# Menghitung korelasi hanya pada kolom angka
correlation = df.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap Korelasi Antar Variabel')
plt.show()

#Heatmap ini menampilkan matriks korelasi antar variabel numerik untuk melihat seberapa kuat hubungan antar fitur data.