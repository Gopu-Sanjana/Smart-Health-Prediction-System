# Smart Health Prediction System

## Overview

The Smart Health Prediction System is a web-based application developed to manage patient records and provide health assessments based on blood test values such as glucose, haemoglobin, and cholesterol levels. The system allows users to perform CRUD operations, validate patient information, and generate AI-assisted health remarks. It was developed using FastAPI, SQLite, SQLAlchemy, HTML, CSS, Bootstrap, JavaScript, and Google Gemini API to demonstrate full-stack web development and AI integration in a healthcare-related application.

---

## Features

- Add new patient records
- View patient records
- Update existing patient information
- Delete patient records
- Generate AI-assisted health remarks
- Input validation
- Persistent data storage using SQLite
- Responsive user interface
- REST API documentation using Swagger UI

---

## Technologies Used

### Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### AI Integration

- Google Gemini API

---

## Patient Information Stored

The application stores the following details:

- Full Name
- Date of Birth
- Email Address
- Glucose Level
- Haemoglobin Level
- Cholesterol Level
- Health Remarks

---

## CRUD Operations

### Create
Add a new patient record to the database.

### Read
Retrieve and display all patient records.

### Update
Modify existing patient information and regenerate health remarks.

### Delete
Remove patient records from the database.

---

## Validation Rules

The application validates:

- Full Name cannot be empty
- Email must be valid
- Date of Birth cannot be a future date
- Glucose value must be greater than zero
- Haemoglobin value must be greater than zero
- Cholesterol value must be greater than zero

---

## Project Structure

Smart-Health-Prediction-System

├── app  
│   ├── __init__.py  
│   ├── database.py  
│   ├── main.py  
│   ├── models  
│   ├── routes  
│   ├── schemas  
│   ├── services  
│   └── utils  
│  
├── database  
│  
├── frontend  
│   ├── index.html  
│   ├── script.js  
│   └── style.css  
│  
├── README.md  
├── requirements.txt  
└── health.db  

---

## API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | /patients | Create Patient |
| GET | /patients | Get All Patients |
| GET | /patients/{id} | Get Patient By ID |
| PUT | /patients/{id} | Update Patient |
| DELETE | /patients/{id} | Delete Patient |

---

## Running the Project

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

.\venv\Scripts\Activate.ps1

### Install Dependencies

pip install -r requirements.txt

### Run Backend Server

uvicorn app.main:app --reload

### API Documentation

http://127.0.0.1:8000/docs

### Run Frontend

Open the frontend folder in VS Code and launch index.html using Live Server.

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Building REST APIs using FastAPI
- Working with SQLAlchemy ORM
- Implementing CRUD operations
- Managing databases using SQLite
- Integrating frontend and backend applications
- Applying input validation techniques
- Using AI APIs in real-world applications
- Developing full-stack web applications

---

## Future Enhancements

- Patient search functionality
- Downloadable health reports
- User authentication
- Dashboard analytics
- Advanced disease prediction models
- Cloud deployment

---

## Author

Sanjana Gopu

