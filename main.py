from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

# Memuat model yang telah dilatih
model = joblib.load('salary_model.pkl')

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model data input disesuaikan menjadi pengalaman kerja (years_experience)
class SalaryData(BaseModel):
    years_experience: float

@app.post("/predict")
def predict_salary(data: SalaryData):
    # Mengambil input dari user
    input_data = np.array([data.years_experience])
    
    # Melakukan prediksi gaji
    prediction = model.predict(input_data.reshape(-1, 1))[0]
    
    # Mengembalikan hasil prediksi dalam format JSON
    return {"predicted_salary": float(prediction)}

# Jalankan dengan: uvicorn main:app --reload