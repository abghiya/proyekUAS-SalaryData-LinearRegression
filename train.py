import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# 1. LOAD DATASET DARI EXCEL
file_path = 'Salary_Data.xlsx'
df = pd.read_excel(file_path)

# 2. DEFINISIKAN VARIABEL
X = df[['YearsExperience']]
y = df['Salary']

# 3. SPLIT DATA (Membagi data menjadi data latih dan data uji)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. TRAIN MODEL (Melatih Model Regresi Linear)
model = LinearRegression()
model.fit(X_train, y_train)

# 5. TESTING SEDERHANA
# Mencoba prediksi untuk pengalaman 5 tahun
dummy_pred = model.predict([[5]])
print(f"Prediksi gaji untuk 5 tahun pengalaman: {dummy_pred[0]}")

# 6. SIMPAN MODEL
joblib.dump(model, 'salary_model.pkl')
print("Model berhasil dilatih dan disimpan dengan nama 'salary_model.pkl'")