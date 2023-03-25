# !Missing Value with Data Transofrmation and Main Function

import pandas as pd 
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

def tampilkan_data():
    data = pd.read_csv("soal.csv")
    print(data)

def hitung_jumlah_missing_value(column_name):
    data = pd.read_csv("soal.csv")
    print(data[column_name].isnull().sum())
    
def count_null(filename, colname):
    # Baca data dari file CSV
    filename = "soal.csv"
    data = pd.read_csv(filename)
    
    # Hitung jumlah nilai null pada setiap kolom yang diminta
    null_counts = data[colname].isnull().sum()
    
    # Tampilkan hasil perhitungan
    print("Jumlah nilai null pada setiap kolom:")
    print(null_counts)

def encode_data():
    data = pd.read_csv("soal.csv")
    data_numerik = data.apply(LabelEncoder().fit_transform)
    print(data_numerik)

def fill_missing_and_encode():
    # Baca data dari file CSV
    data = pd.read_csv('soal.csv')
    
    # Tampilkan kolom-kolom dengan missing value
    missing_cols = data.columns[data.isnull().any()].tolist()
    print("Kolom-kolom dengan missing value:", missing_cols)
    
    # Isi missing value dengan nilai rata-rata atau mode pada setiap kolom yang sesuai
    for col in missing_cols:
        if data[col].dtype == np.number:
            fill_value = data[col].mean()
        else:
            fill_value = data[col].mode()[0]
        data[col].fillna(value=fill_value, inplace=True)
    
    # Lakukan label encoding pada semua kolom
    le = LabelEncoder()
    data_encoded = data.apply(le.fit_transform)
    
    # Tampilkan hasil encoding sebagai dataframe
    print(data_encoded)

def scale_data():
    data = pd.read_csv("soal.csv")
    scaler = MinMaxScaler()
    data_scaled = pd.DataFrame(scaler.fit_transform(data))
    print(data_scaled)

def encode_and_scale_data():
    # Baca data dari file CSV
    filename = "soal.csv"
    data = pd.read_csv(filename)
    
    # Lakukan label encoding untuk setiap kolom
    # le = LabelEncoder()
    missing_cols = data.columns[data.isnull().any()].tolist()
    print("Kolom-kolom dengan missing value:", missing_cols)
    
    # Isi missing value dengan nilai rata-rata atau mode pada setiap kolom yang sesuai
    for col in missing_cols:
        if data[col].dtype == np.number:
            fill_value = data[col].mean()
        else:
            fill_value = data[col].mode()[0]
        data[col].fillna(value=fill_value, inplace=True)
    
    # Lakukan label encoding pada semua kolom
    le = LabelEncoder()
    data_encoded = data.apply(le.fit_transform)
    # data_encoded = fill_missing_and_encode()
    
    # Lakukan feature scaling menggunakan MinMaxScaler
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data_encoded)
    
    # Tampilkan hasil scaling sebagai dataframe
    df_scaled = pd.DataFrame(data_scaled, columns=data.columns)
    print(df_scaled)

    
# membaca data dari file csv
data = pd.read_csv("soal.csv")

while True:
    print("Menu:")
    print("a. Menampilkan data asli")
    print("b. Tampilkan jumlah missing value(null) pada setiap kolom sesuai inputan dari user")
    print("c. Tampilkan data setelah dilakukan perubahan dari non numerik menjadi numerik")
    print("d. Tampilkan data hasil feature scaling")
    print("e. Keluar")

    choice = input("Masukkan pilihan: ")

    if choice == "a":
        tampilkan_data()
    elif choice == "b":
          hitung_jumlah_missing_value(column_name)
    elif choice == "c":
          fill_missing_and_encode()
    elif choice == "d":
          encode_and_scale_data()
    elif choice == "e":
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi")
    
