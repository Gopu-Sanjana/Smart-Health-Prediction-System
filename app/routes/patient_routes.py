from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.patient import Patient
from app.schemas.patient_schema import PatientCreate
from app.services.ai_service import generate_ai_remark

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE
@router.post("/patients")
def create_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):

    remarks = generate_ai_remark(
    patient.glucose,
    patient.haemoglobin,
    patient.cholesterol
)

    new_patient = Patient(
        full_name=patient.full_name,
        date_of_birth=patient.date_of_birth,
        email=patient.email,
        glucose=patient.glucose,
        haemoglobin=patient.haemoglobin,
        cholesterol=patient.cholesterol,
        remarks=remarks
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient


# READ ALL
@router.get("/patients")
def get_patients(
    db: Session = Depends(get_db)
):
    return db.query(Patient).all()


# READ ONE
@router.get("/patients/{patient_id}")
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


# UPDATE
@router.put("/patients/{patient_id}")
def update_patient(
    patient_id: int,
    patient_data: PatientCreate,
    db: Session = Depends(get_db)
):

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    patient.full_name = patient_data.full_name
    patient.date_of_birth = patient_data.date_of_birth
    patient.email = patient_data.email
    patient.glucose = patient_data.glucose
    patient.haemoglobin = patient_data.haemoglobin
    patient.cholesterol = patient_data.cholesterol

    patient.remarks = generate_ai_remark(
    patient.glucose,
    patient.haemoglobin,
    patient.cholesterol
)

    db.commit()

    return {
        "message": "Patient updated successfully"
    }


# DELETE
@router.delete("/patients/{patient_id}")
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    db.delete(patient)
    db.commit()

    return {
        "message": "Patient deleted successfully"
    }