from sqlalchemy import Column, Integer, Date,String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from db.base import Base

class Production(Base):
    __tablename__ = "productions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    product_name = Column(String)
    date = Column(Date)
    quantity_produced = Column(Integer)
    # Define relationship to access related employee information
    employee = relationship("Employee", back_populates="productions")

class create_update_production(BaseModel):
    product_name :  str
    quantity_produced : int