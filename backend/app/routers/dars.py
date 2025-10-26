from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date

from app.core.deps import get_db
from app.models.dar import DailyActivityReport
from app.schemas.dar_schema import DARCreate, DAROut

router = APIRouter(prefix="/dars", tags=["Daily Activity Reports"])

@router.post("", response_model=DAROut, status_code=status.HTTP_201_CREATED)
def create_dar(payload: DARCreate, db: Session = Depends(get_db)):
    new_dar = DailyActivityReport(
        date=payload.date or date.today(),
        shift=payload.shift,
        summary=payload.summary,
        guard_id=payload.guard_id
    )
    
    db.add(new_dar)
    db.commit()
    db.refresh(new_dar)
    return new_dar

@router.get("", response_model=List[DAROut])
def list_dars(
    db: Session = Depends(get_db),
    guard_id: Optional[int] = Query(None, description="Filter by guard ID"),
    report_date: Optional[date] = Query(None, description="Filter by report date"),
    shift: Optional[str] = Query(None, description="Filter by shift name")
):

    query = db.query(DailyActivityReport)
    
    if guard_id:
        query = query.filter(DailyActivityReport.guard_id == guard_id)
    if report_date:
        query = query.filter(DailyActivityReport.date == report_date)
    if shift:
        query = query.filter(DailyActivityReport.shift.ilike(f"%{shift}%"))
        
    return query.all()

@router.get("/{dar_id}", response_model=DAROut)
def get_dar(dar_id: int, db: Session = Depends(get_db)):
    dar = db.query(DailyActivityReport).get(dar_id)
    if not dar:
        raise HTTPException(status_code=404, detail="report not found")
    return dar

@router.delete("/{dar_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dar(dar_id: int, db: Session = Depends(get_db)):
    dar = db.query(DailyActivityReport).get(dar_id)
    if not dar:
        raise HTTPException(status_code=404, detail="report not found")
    db.delete(dar)
    db.commit()
    return None