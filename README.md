# Proyek UAS Machine Learning - Prediksi Gaji Berdasarkan Pengalaman Kerja

Proyek ini merupakan implementasi Machine Learning end-to-end untuk memprediksi gaji karyawan berdasarkan jumlah tahun pengalaman kerja menggunakan algoritma **Simple Linear Regression**.

## Komponen Proyek
- **Dataset**: `Salary_Data.xlsx` (Data pengalaman kerja dan gaji).
- **Model Training**: `train.py` (Proses preprocessing dan pelatihan model).
- **Backend API**: `main.py` (Menggunakan FastAPI untuk melayani prediksi).
- **Frontend**: `index.html` (Antarmuka web menggunakan Tailwind CSS dan JavaScript).

## Cara Menjalankan Proyek

1. **Persiapan Lingkungan (Virtual Environment):**
   ```bash
   python -m venv .venv
   # Untuk Windows:
   .venv\Scripts\activate
   # Untuk Mac/Linux:
   source .venv/bin/activate