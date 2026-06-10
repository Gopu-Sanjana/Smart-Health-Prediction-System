from pydantic import BaseModel
from pydantic import EmailStr


class PatientCreate(BaseModel):

    full_name: str
    date_of_birth: str
    email: EmailStr
    glucose: float
    haemoglobin: float
    cholesterol: float


class PatientResponse(PatientCreate):

    id: int
    remarks: str

    class Config:
        from_attributes = True