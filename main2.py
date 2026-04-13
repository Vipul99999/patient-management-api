from fastapi import FastAPI, HTTPException, Path, Query
import json
import os

app = FastAPI()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "patients.json")



def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except:
        return {"patients": []}


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)




@app.get("/")
def home():
    return {"message": "Patient Management API 🚀"}


#  Get all patients with Query filters
@app.get("/patients")
def get_all_patients(
    gender: str = Query(None, description="Filter by gender"),
    min_age: int = Query(None, ge=0, description="Minimum age"),
    max_age: int = Query(None, ge=0, description="Maximum age")
):
    data = load_data()
    patients = data["patients"]

    # Apply filters
    if gender:
        patients = [p for p in patients if p["gender"].lower() == gender.lower()]

    if min_age is not None:
        patients = [p for p in patients if p["age"] >= min_age]

    if max_age is not None:
        patients = [p for p in patients if p["age"] <= max_age]

    return {"patients": patients}


# Get patient by ID (Path param)
@app.get("/patients/{patient_id}")
def get_patient(
    patient_id: int = Path(..., gt=0, description="ID must be greater than 0")
):
    data = load_data()
    for patient in data["patients"]:
        if patient["id"] == patient_id:
            return patient

    raise HTTPException(status_code=404, detail="Patient not found")


# Add patient
@app.post("/patients")
def add_patient(patient: dict):
    data = load_data()

    if data["patients"]:
        new_id = max(p["id"] for p in data["patients"]) + 1
    else:
        new_id = 1

    patient["id"] = new_id
    data["patients"].append(patient)

    save_data(data)

    return {"message": "Patient added", "patient": patient}


#  Update patient
@app.put("/patients/{patient_id}")
def update_patient(
    patient_id: int = Path(..., gt=0),
    updated_data: dict = {}
):
    data = load_data()

    for i, patient in enumerate(data["patients"]):
        if patient["id"] == patient_id:
            updated_data["id"] = patient_id
            data["patients"][i] = updated_data
            save_data(data)
            return {"message": "Patient updated", "patient": updated_data}

    raise HTTPException(status_code=404, detail="Patient not found")


#  Delete patient
@app.delete("/patients/{patient_id}")
def delete_patient(
    patient_id: int = Path(..., gt=0)
):
    data = load_data()

    for i, patient in enumerate(data["patients"]):
        if patient["id"] == patient_id:
            deleted = data["patients"].pop(i)
            save_data(data)
            return {"message": "Patient deleted", "patient": deleted}

    raise HTTPException(status_code=404, detail="Patient not found")


#  Advanced Query Example (search)
@app.get("/search")
def search_patients(
    name: str = Query(None, min_length=1, description="Search by name"),
    city: str = Query(None, description="Filter by city")
):
    data = load_data()
    patients = data["patients"]

    if name:
        patients = [p for p in patients if name.lower() in p["name"].lower()]

    if city:
        patients = [p for p in patients if city.lower() == p["city"].lower()]

    return {"results": patients}