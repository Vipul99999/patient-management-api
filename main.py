from fastapi import FastAPI, HTTPException
import json
import os

app = FastAPI()

# File path setup
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


@app.get("/patients")
def get_all_patients():
    return load_data()


@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    data = load_data()
    for patient in data["patients"]:
        if patient["id"] == patient_id:
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")


@app.post("/patients")
def add_patient(patient: dict):
    data = load_data()

    # Generate new ID
    if data["patients"]:
        new_id = max(p["id"] for p in data["patients"]) + 1
    else:
        new_id = 1

    patient["id"] = new_id
    data["patients"].append(patient)

    save_data(data)

    return {"message": "Patient added successfully", "patient": patient}


@app.put("/patients/{patient_id}")
def update_patient(patient_id: int, updated_data: dict):
    data = load_data()

    for i, patient in enumerate(data["patients"]):
        if patient["id"] == patient_id:
            updated_data["id"] = patient_id
            data["patients"][i] = updated_data
            save_data(data)
            return {"message": "Patient updated", "patient": updated_data}

    raise HTTPException(status_code=404, detail="Patient not found")


@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):
    data = load_data()

    for i, patient in enumerate(data["patients"]):
        if patient["id"] == patient_id:
            deleted = data["patients"].pop(i)
            save_data(data)
            return {"message": "Patient deleted", "patient": deleted}

    raise HTTPException(status_code=404, detail="Patient not found")