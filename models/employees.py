from db.base import Base
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey, Uuid, TIMESTAMP
from sqlalchemy.orm import relationship
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    uuid = Column(Uuid)
    name = Column(String(30))
    golongan = Column(String(30))
    updated_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)
    fingerprint = Column(String)

    presences = relationship("Presensi", back_populates="employee")


class CreateUpdateEmployee(BaseModel):
    name: str
    golongan: str
    fingerprint: str
