from decouple import config

DATABASE_URL = config("DATABASE_URL")

SUPABASE_URL = config("SUPABASE_URL")

SUPABASE_KEY = config("SUPABASE_KEY")

GEMINI_API_KEY = config("GEMINI_API_KEY", default="")
