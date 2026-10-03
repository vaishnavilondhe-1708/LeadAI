from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models.lead import Lead
from app.routers.lead_router import router as lead_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="LeadPilot AI",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routes
app.include_router(lead_router)


@app.get("/")
def root():
    return {
        "message": "LeadPilot AI Backend Running 🚀"
    }
