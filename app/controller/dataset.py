import pandas as pd
import numpy as np
from app.utils.random_forest import format_rupiah

def getDataset():
    data = pd.read_csv('G:\My Drive\dataset\houseprediction\jakarta-house-data.csv') 
    return data

def getDatasetArray():
    data = getDataset()
    data = data.to_numpy()
    return data

def cardData():
    data = getDataset()
    df = pd.DataFrame(data)
    maxPrice = format_rupiah(df['Harga'].max())
    minPrice = format_rupiah(df['Harga'].min())
    totalRow = len(data)
    cardData = [totalRow,maxPrice,minPrice]
    return cardData

