from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class DataModel(BaseModel):
    image: str
    hospital: str
    doctor: str
    experience: str
    rating: str
    fees: str
    button: str

# Dummy Data
dummy_doctors = [
    DataModel(
        image="https://example.com/doctor1.jpg",
        hospital="Apollo Hospital",
        doctor="Dr. A Sharma",
        experience="10 years",
        rating="4.8",
        fees="$50",
        button="Book Now"
    ),
    DataModel(
        image="https://example.com/doctor2.jpg",
        hospital="Fortis Hospital",
        doctor="Dr. B Verma",
        experience="8 years",
        rating="4.5",
        fees="$40",
        button="Book Now"
    ),
    DataModel(
        image="https://example.com/doctor3.jpg",
        hospital="Max Healthcare",
        doctor="Dr. C Gupta",
        experience="12 years",
        rating="4.9",
        fees="$60",
        button="Book Now"
    )
]

@app.get("/doctors", response_model=List[DataModel])
def get_doctors():
    return dummy_doctors

@app.get("/")
def read_root():
    return {"message": "Welcome to the Doctor API! Access /doctors for data."}

