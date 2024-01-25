import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split, cross_val_score

# Load dataset
file_path = 'G:/My Drive/dataset/houseprediction/jakarta-house-data.csv'
data = pd.read_csv(file_path)

# Mengganti NaN dengan median kolom 'carport'
median_value = data['Carport'].median()
data['Carport'].fillna(median_value, inplace=True)

# Hapus data yang kosong
data = data.dropna(subset=['Kamar Tidur','Kamar Mandi','Luas Tanah','Luas Bangunan','Jumlah Lantai'])

# Memisahkan fitur dan target
X = data.drop(['Harga','Tanggal Scrap','Terjangkau Internet','Lokasi'], axis=1)  # Menghapus kolom 'harga' sebagai target
y = data['Harga']

# Memisahkan data menjadi data latih (80%) dan data validasi (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing fitur numerik dengan StandardScaler
numeric_features = ['Kamar Tidur','Kamar Mandi','Luas Tanah','Luas Bangunan','Jumlah Lantai']
numeric_transformer = StandardScaler()

# Preprocessing fitur kategorikal dengan One-Hot Encoding
categorical_features = ['Kota']
categorical_transformer = OneHotEncoder()

# Menggabungkan preprocessing fitur numerik dan kategorikal
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

print('Total data training = ' + str(len(X_train)))
print('Total data uji = ' + str(len(X_test)))

# Melakukan preprocessing pada data train dan uji
X_train_preprocessed = preprocessor.fit_transform(X_train)
X_test_preprocessed = preprocessor.transform(X_test)
# X_test_preprocessed = preprocessor.transform(X_test)

# Membuat model Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=13)
# model = RandomForestRegressor(n_estimators=700, max_depth=50, min_samples_split=5, min_samples_leaf=2, max_features='sqrt', random_state=42)


# Melatih model menggunakan data latih
model.fit(X_train_preprocessed, y_train)

# Memprediksi harga rumah menggunakan data uji
y_test_pred = model.predict(X_test_preprocessed)

cv_scores = cross_val_score(model, X_train_preprocessed, y_train, cv=2, scoring='neg_mean_squared_error')
# Menghitung MSE rata-rata dari cross-validation
average_mse_cv = -cv_scores.mean()
print("Mean Squared Error (Cross-Validation):", round(average_mse_cv, 2))

# Evaluasi model menggunakan mean squared error (MSE) pada data training
print("Rsquare Score (Train):", model.score(X_train_preprocessed, y_train))

# Evaluasi model menggunakan r2_score pada data uji
mse_test = r2_score(y_test, y_test_pred)
print("Rsquare Score (Test):", mse_test)

# Menghitung Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_test_pred)
print(f'MAE: {mae}')
# print(format_rupiah(mae))

# Menghitung Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_test_pred)
print(f'MSE: {mse}')

# Menghitung R-Squared
r_squared = r2_score(y_test, y_test_pred)
print(f'R-Squared: {r_squared}')

def format_rupiah(angka):
    rupiah = "Rp " + "{:,.0f}".format(angka).replace(",", ".")
    return rupiah

# Contoh prediksi harga rumah baru
def house_prediction(kota,kamarTidur,kamarMandi,luasTanah,luasBangunan,carport,jumlahLantai,terjangkauInternet):
    new_data = pd.DataFrame([[kota,kamarTidur,kamarMandi,luasTanah,luasBangunan,carport,jumlahLantai,terjangkauInternet]], columns=['Kota','Kamar Tidur','Kamar Mandi','Luas Tanah','Luas Bangunan','Carport', 'Jumlah Lantai','Terjangkau Internet'])
    new_data_scaled = preprocessor.transform(new_data)  # Melakukan preprocessing pada data baru
    predicted_price = model.predict(new_data_scaled)
    message = format_rupiah(int(predicted_price))
    return message