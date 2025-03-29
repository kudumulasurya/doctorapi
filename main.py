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
        image="https://images.pexels.com/photos/8376265/pexels-photo-8376265.jpeg",
        hospital="Apollo Hospital",
        doctor="Dr. A Sharma",
        experience="Ophthalmologist/Eye Surgeon • 14 years experience overall",
        rating="★★★★ 35 reviews",
        fees="$50",
        button="Book Now"
    ),
    DataModel(
        image="https://images.pexels.com/photos/3825586/pexels-photo-3825586.jpeg",
        hospital="Fortis Hospital",
        doctor="Dr. B Verma",
        experience="Cardiologist • 20 years experience overall",
        rating="★★★★★ 50 reviews",
        fees="$70",
        button="Book Now"
    ),
    DataModel(
        image="https://images.pexels.com/photos/5327580/pexels-photo-5327580.jpeg",
        hospital="Max Healthcare",
        doctor="Dr. C Gupta",
        experience="Dermatologist • 10 years experience overall",
        rating="★★★☆ 25 reviews",
        fees="$40",
        button="Book Now"
    ),
    DataModel(
        image="https://images.pexels.com/photos/8460157/pexels-photo-8460157.jpeg",
        hospital="AIIMS Delhi",
        doctor="Dr. D Kapoor",
        experience="Neurologist • 18 years experience overall",
        rating="★★★★★ 60 reviews",
        fees="$90",
        button="Book Now"
    ),
    DataModel(
        image="https://images.pexels.com/photos/8460275/pexels-photo-8460275.jpeg",
        hospital="Medanta Hospital",
        doctor="Dr. E Mehta",
        experience="Orthopedic Surgeon • 15 years experience overall",
        rating="★★★★☆ 42 reviews",
        fees="$65",
        button="Book Now"
    ),
    DataModel(
        image="https://images.pexels.com/photos/5327640/pexels-photo-5327640.jpeg",
        hospital="Manipal Hospital",
        doctor="Dr. F Rao",
        experience="ENT Specialist • 12 years experience overall",
        rating="★★★★ 33 reviews",
        fees="$55",
        button="Book Now"
    ),
    DataModel(
        image="https://images.pexels.com/photos/8376266/pexels-photo-8376266.jpeg",
        hospital="Columbia Asia Hospital",
        doctor="Dr. G Nair",
        experience="General Physician • 22 years experience overall",
        rating="★★★★★ 78 reviews",
        fees="$60",
        button="Book Now"
    ),
    DataModel(
        image="https://images.pexels.com/photos/8460155/pexels-photo-8460155.jpeg",
        hospital="Narayana Health",
        doctor="Dr. H Das",
        experience="Oncologist • 17 years experience overall",
        rating="★★★☆ 29 reviews",
        fees="$85",
        button="Book Now"
    ),
    DataModel(
        image="https://images.pexels.com/photos/5327657/pexels-photo-5327657.jpeg",
        hospital="CMC Vellore",
        doctor="Dr. I Sen",
        experience="Psychiatrist • 11 years experience overall",
        rating="★★★★☆ 38 reviews",
        fees="$45",
        button="Book Now"
    ),
    DataModel(
        image="https://images.pexels.com/photos/8460156/pexels-photo-8460156.jpeg",
        hospital="Kokilaben Hospital",
        doctor="Dr. J Pillai",
        experience="Pulmonologist • 13 years experience overall",
        rating="★★★★ 32 reviews",
        fees="$50",
        button="Book Now"
    )
]


@app.get("/doctors", response_model=List[DataModel])
def get_doctors():
    return dummy_doctors

@app.get("/")
def read_root():
    return {"message": "Welcome to the Doctor API! Access /doctors for data."}

