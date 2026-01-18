# Proyek UAS Machine Learning - Prediksi Gaji Karyawan IT

Proyek ini merupakan implementasi *Machine Learning* secara *end-to-end* yang dirancang untuk memprediksi **gaji karyawan di bidang IT** berdasarkan jumlah tahun pengalaman kerja menggunakan algoritma **Simple Linear Regression**.

## Komponen Proyek

* **Dataset**: `Salary_Data.xlsx` (Data pengalaman kerja dan gaji karyawan IT).
* **Model Training**: `train.py` (Proses preprocessing dan pelatihan model).
* **Backend API**: `main.py` (Menggunakan FastAPI untuk melayani prediksi).
* **Frontend**: `index.html` (Antarmuka web menggunakan Tailwind CSS dan JavaScript).

## Cara Menjalankan Proyek

### 1. Persiapan Lingkungan (Virtual Environment)
```bash
# Untuk Windows:
python -m venv .venv
.venv\Scripts\activate

# Untuk macOS (iMac/MacBook):
python3 -m venv .venv
source .venv/bin/activate

# Instalasi dependensi
pip install -r requirements.txt

# Melatih Model (Windows)
python train.py

# Melatih Model (macOS/iMac)
python3 train.py

# Jalankan Server
uvicorn main:app --reload

# Akses Aplikasi:
# - Frontend: Buka file index.html di browser.
# - Swagger UI: Akses [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)