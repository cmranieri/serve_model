from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load your model (students: make sure model.pkl exists!)
model = joblib.load("model.pkl")

# Create a FastAPI app instance
app = FastAPI(title="ML Model API")

# Define the expected input data schema
class InputData(BaseModel):
    mean_radius: float
    mean_texture: float
    mean_smoothness: float

# Define a health check route
@app.get("/health")
def health_check():
    return {"status": "alive"}

# Define the prediction route
@app.post("/predict")
def predict(data: InputData):
    try:
        input_vector = np.array([[data.mean_radius, data.mean_texture, data.mean_smoothness]])
        prediction = model.predict(input_vector)
        return {"prediction": str(prediction)}
    except Exception as e:
        return {"error": str(e)}

