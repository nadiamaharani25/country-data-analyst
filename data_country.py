import pandas as pd
df = pd.read_csv('countries of the world.csv')
import matplotlib.pyplot as plt


#1. Cek struktur data (Mencari Informasi seluruh data)
print(df.info())
print('\n')


#2. Cek 5 baris pertama
print(df.head())
print('\n')


#3. Periksa apakah ada null atau tidak untuk 'GDP ($ per capita)'
gdp = len(df[pd.isnull(df['GDP ($ per capita)'])])
print(gdp)
print('\n')


#4. Kalau ada, bersihkan data (cleaning) menggunakan fillna
df['GDP ($ per capita)'].fillna(-1, inplace = True)
print('\n')


#5. Periksa apakah ada null atau tidak untuk 'Literacy'
literacy = len(df[pd.isnull(df['Literacy (%)'])])
print(literacy)
print('\n')


#6. Kalau ada, bersihkan data (cleaning) menggunakan fillna
df['Literacy (%)'].fillna(-1, inplace = True)
print(df.info())
print('\n')


#7. Bersihkan data (Kadang dataset ini punya format angka sebagai string)
# kalau ada teks aneh → ubah jadi NaN.
# bersihkan literacy
print('Sebelum di replace')
print(df['Literacy (%)'])
df['Literacy (%)'] = df['Literacy (%)'].str.replace(',', '.')
df['Literacy (%)'] = df['Literacy (%)'].apply(float)

print('Setelah di replace')
print(df['Literacy (%)'])


#8. Visualisasi Data (Scatter Plot) -> Hubungan 2 variabel
#GDP per capita → rata-rata pendapatan/kemakmuran suatu negara
#Literacy rate → persentase penduduk yang bisa membaca dan menulis
#Tujuannya biasanya untuk mencari tahu:
#“Apakah negara yang tingkat literasinya tinggi cenderung punya GDP lebih tinggi?”
df.plot.scatter(x = 'Literacy (%)', y = 'GDP ($ per capita)')
plt.show()


