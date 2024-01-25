import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
file_path = 'G:/My Drive/dataset/houseprediction/jakarta-house-data.csv'
data = pd.read_csv(file_path)

column = ['Harga','Kamar Tidur','Kamar Mandi','Luas Tanah','Luas Bangunan','Carport','Jumlah Lantai']

def heatmap():
    plt.figure(figsize=(15,10))
    heatmap = sns.heatmap(data[column].corr(),annot=True)
    heatmap.set_title('Gambar 1', fontdict={'fontsize': 18}, pad=16)
    plt.savefig('app/storage/heatmap.png',bbox_inches='tight')
    return "Berhasil mengupdate heatmap"

def heatmapByPrice():
    plt.figure(figsize=(8, 12))  # Menyesuaikan ukuran gambar
    heatmap = sns.heatmap(data[column].corr()[['Harga']].sort_values(by='Harga', ascending=False),
                          vmin=-1, vmax=1, annot=True, cmap='BrBG')  # Mengganti menaik=False menjadi ascending=False
    heatmap.set_title('Gambar 2', fontdict={'fontsize': 18}, pad=16)
    plt.savefig('app/storage/heatmapbyprice.png',bbox_inches='tight')
    return "Berhasil mengupdate heatmap berdasarkan harga"