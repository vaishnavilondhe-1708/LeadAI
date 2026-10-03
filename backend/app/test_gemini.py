from types import SimpleNamespace

from app.services.gemini_service import analyze_lead

# Dummy lead for testing
lead = SimpleNamespace(
    company="FlytBase",
    industry="Drone Automation",
    company_size="50-100",
    country="India",
    lead_source="Hackathon"
)

result = analyze_lead(lead)

print(result)