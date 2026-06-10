from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from app.database import Base


class Patient(Base):

    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    date_of_birth = Column(String(20), nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    glucose = Column(Float, nullable=False)

    haemoglobin = Column(Float, nullable=False)

    cholesterol = Column(Float, nullable=False)

    remarks = Column(String(500))