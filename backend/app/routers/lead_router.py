from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.lead import LeadCreate, LeadResponse
from app.services.lead_service import create_lead, get_all_leads

router = APIRouter(
    prefix="/leads",
    tags=["Leads"]
)


@router.post("/", response_model=LeadResponse)
def add_lead(
    lead: LeadCreate,
    db: Session = Depends(get_db)
):
    return create_lead(db, lead)


@router.get("/", response_model=list[LeadResponse])
def fetch_all_leads(
    db: Session = Depends(get_db)
):
    return get_all_leads(db)