import json

from google import genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def analyze_lead(lead):
    prompt = f"""
You are an expert B2B sales lead analyst.

Analyze this lead.

Company: {lead.company}
Industry: {lead.industry}
Company Size: {lead.company_size}
Country: {lead.country}
Lead Source: {lead.lead_source}

Return ONLY valid JSON:

{{
    "score": 90,
    "priority": "High",
    "assigned_to": "Enterprise Sales",
    "reason": "Short explanation"
}}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)