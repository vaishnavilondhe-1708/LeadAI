from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)

    # Lead Information
    company = Column(String, nullable=False)
    contact_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    industry = Column(String, nullable=False)
    company_size = Column(String, nullable=False)
    country = Column(String, nullable=False)
    lead_source = Column(String, nullable=False)

    # AI Analysis
    score = Column(Integer, default=0)
    priority = Column(String, default="Low")
    assigned_to = Column(String, default="Unassigned")
    ai_reason = Column(Text, nullable=True)

    # Lead Status
    status = Column(String, default="New")