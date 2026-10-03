from pydantic import BaseModel, EmailStr, ConfigDict


class LeadCreate(BaseModel):
    company: str
    contact_name: str
    email: EmailStr
    industry: str
    company_size: str
    country: str
    lead_source: str


class LeadResponse(BaseModel):
    id: int
    company: str
    contact_name: str
    email: EmailStr
    industry: str
    company_size: str
    country: str
    lead_source: str

    # AI Analysis
    score: int
    priority: str
    assigned_to: str
    ai_reason: str | None = None

    # Lead Status
    status: str

    model_config = ConfigDict(from_attributes=True)