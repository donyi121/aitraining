from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import numpy as np
import pickle

app = FastAPI()

# Load pkl files
with open("kmeans.pkl", "rb") as f:
    kmeans = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

segment_map = {
    0: "Budget Housing",
    1: "Mid-Range Housing",
    2: "Premium Housing",
    3: "Luxury Housing"
}

class HouseInput(BaseModel):
    size: float
    bhk: int
    location: float
    price_cr: float


@app.post("/predict")
def predict_cluster(data: HouseInput):
    price = data.price_cr * 10000000
    input_data = np.array([[data.size, data.bhk, data.location, price]])
    input_scaled = scaler.transform(input_data)

    cluster = int(kmeans.predict(input_scaled)[0])
    segment = segment_map.get(cluster, "Unknown")

    posters = {
        "Budget Housing": "/static/images/budget.png",
        "Mid-Range Housing": "/static/images/midrange.png",
        "Premium Housing": "/static/images/premium.png",
        "Luxury Housing": "/static/images/luxury.png"
    }

    return {
        "segment": segment,
        "poster": posters.get(segment, "/static/default.png")
    }


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("templates/index.html")
