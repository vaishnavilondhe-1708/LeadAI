from sqlalchemy.orm import Session

from app.models.lead import Lead
from app.schemas.lead import LeadCreate
from app.services.gemini_service import analyze_lead


def create_lead(db: Session, lead: LeadCreate):
    # Analyze lead using Gemini
    analysis = analyze_lead(lead)

    db_lead = Lead(
        company=lead.company,
        contact_name=lead.contact_name,
        email=lead.email,
        industry=lead.industry,
        company_size=lead.company_size,
        country=lead.country,
        lead_source=lead.lead_source,

        score=analysis["score"],
        priority=analysis["priority"],
        assigned_to=analysis["assigned_to"],
        ai_reason=analysis["reason"],
    )

    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)

    return db_lead


def get_all_leads(db: Session):
    return db.query(Lead).all()


def get_lead_by_id(db: Session, lead_id: int):
    return db.query(Lead).filter(Lead.id == lead_id).first()