from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.core.deps import get_db
from app.models.incident import Incident
from app.schemas.incident_schema import IncidentCreate, IncidentOut

router = APIRouter(prefix="/incidents", tags=["incidents"])

@router.post("", response_model=IncidentOut, status_code=status.HTTP_201_CREATED)
def create_incident(payLoad: IncidentCreate, db: Session = Depends(get_db)):
    new_incident = Incident(
        title=payLoad.title,
        description=payLoad.description,
        severity=payLoad.severity,
        location=payLoad.location,
        date_reported=datetime.utcnow(),
        guard_id=payLoad.guard_id
    )
    
    db.add(new_incident)
    db.commit()
    db.refresh(new_incident)
    return new_incident

@router.get("", response_model=List[IncidentOut])
def list_incidents(db: Session = Depends(get_db)):
    return db.query(Incident).all()

@router.get("/{incident_id}", response_model=IncidentOut)
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    incident = db.query(Incident).get(incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident

@router.delete("/{incident_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_incident(incident_id: int, db: Session = Depends(get_db)):
    incident = db.query(Incident).get(incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    
    db.delete(incident)
    db.commit()
    return None