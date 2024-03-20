from typing import Union

from fastapi import FastAPI
from typing import Annotated
from fastapi import HTTPException
from fastapi import FastAPI, Request, status, Form
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from db.base import Base
from db.session import engine, SessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session
from models.employees import Employee, CreateUpdateEmployee
from models.presences import Presensi

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/employees")
def get_all_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()


@app.post("/employees")
def create_employees(employee: CreateUpdateEmployee, db: Session = Depends(get_db)):
    db.add(Employee(name=employee.name, golongan=employee.golongan, fingerprint=employee.fingerprint, salary=employee.salary))
    db.commit()
    return {"message": "employees created successfully."}


@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: CreateUpdateEmployee, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="employee not found")
    db_employee.name = employee.name
    db_employee.golongan = employee.golongan
    db_employee.fingerprint = employee.fingerprint
    db_employee.salary = employee.salary

    db.commit()
    return {"message": "employee updated successfully."}


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="employee not found")
    
    db.delete(db_employee)
    db.commit()
    return {"message": "employee deleted successfully."}

@app.get("/presences")
def get_all_presences(db: Session = Depends(get_db)):
    return db.query(Presensi).all()

# @app.post("/presence")
# def create_presence(employee_id: int, db: Session = Depends(get_db)):
    

