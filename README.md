
# 🚀 Patient Management API

A simple and scalable REST API built using FastAPI to manage patient records.  
This project demonstrates CRUD operations using a JSON file as a data source.

---

## 📌 Features

- ✅ Get all patients
- ✅ Get patient by ID
- ✅ Add new patient
- ✅ Update patient details
- ✅ Delete patient
- ✅ JSON-based storage (no database required)
- ✅ Auto API documentation (Swagger UI)

---

## 🛠️ Tech Stack

- Python 3.12+
- FastAPI
- Uvicorn

---

## 📂 Project Structure

```

project/
│── main.py
│── patients.json
│── README.md

````

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/patient-management-api.git
cd patient-management-api
````

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn
```

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

App will run at:

```
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI provides built-in interactive docs:

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📌 API Endpoints

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| GET    | /              | Welcome message   |
| GET    | /patients      | Get all patients  |
| GET    | /patients/{id} | Get patient by ID |
| POST   | /patients      | Add new patient   |
| PUT    | /patients/{id} | Update patient    |
| DELETE | /patients/{id} | Delete patient    |

---

## 🧪 Sample Patient Data

```json
{
  "name": "John Doe",
  "age": 30,
  "gender": "Male",
  "diagnosis": "Flu",
  "city": "New York",
  "country": "USA",
  "height": 180,
  "weight": 80
}
```

---
# In main2.py file we have
Path Parameters
patient_id: int = Path(..., gt=0)

✔ Required
✔ Validation (must be > 0)

✅ 2. Query Parameters
gender: str = Query(None)
min_age: int = Query(None, ge=0)

👉 Example:

/patients?gender=Male&min_age=20
  3. Filtering Logic

You can now:

Filter by gender
Filter by age range
Search by name
🧪 Example URLs
 
👉 All patients
```
http://127.0.0.1:8000/patients
```

👉 Filter
```
http://127.0.0.1:8000/patients?gender=Male&min_age=25
```
👉 Search
```
http://127.0.0.1:8000/search?name=john
🧠 What You Learned (Important)
```
We now used here :
```
✔ Path() → URL parameters
✔ Query() → filters/search
✔ Validation (gt, ge, min_length)
✔ Real API behavior
```

## ⚠️ Notes

* This project uses a JSON file instead of a database (for learning purposes).
* Not suitable for production use.
* Data will reset if the file is modified manually.

---

## 🚀 Future Improvements

* 🔹 Add database (SQLite / PostgreSQL)
* 🔹 Implement authentication (JWT)
* 🔹 Use Pydantic models for validation
* 🔹 Modular project structure
* 🔹 Docker support

---

## 👨‍💻 Author

Vipul Kumar Patel

---

## 📄 License

This project is open-source and available under the MIT License.

```