from db.base import Base
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Presensi(Base):
    __tablename__ = "presences"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    employee_id = Column(ForeignKey("employees.id"), nullable=False) 
    date = Column(Date)
    check_in_time = Column(Time)
    check_out_time = Column(Time)
    employee = relationship("Employee", back_populates="presences")
class Create_presensi(BaseModel):
    check_in : str
    check_out : str
