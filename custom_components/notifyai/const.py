DOMAIN = "notifyai"
CONF_API_KEY = "api_key"
CONF_MODEL = "model"
CONF_NOTIFY_SERVICE_1 = "notify_service_1"
CONF_NOTIFY_SERVICE_2 = "notify_service_2"
CONF_NOTIFY_SERVICE_3 = "notify_service_3"
CONF_NOTIFY_SERVICE_4 = "notify_service_4"

# AI Provider Configuration
CONF_AI_PROVIDER = "ai_provider"
CONF_GROQ_API_KEY = "groq_api_key"

AI_PROVIDERS = {
    "gemini": "Google Gemini (1500/gün)",
    "groq": "Groq (14,400/gün, Çok Hızlı)"
}

# Gemini Models
MODEL_OPTIONS = {
    "gemini-2.5-flash": "Gemini 2.5 Flash (15 RPM, 1500/gün - Tahmini)",
    "gemini-2.5-pro": "Gemini 2.5 Pro (2 RPM, 50/gün - Tahmini)",
    "gemini-2.0-flash-exp": "Gemini 2.0 Flash Exp (10 RPM, 1000/gün - Tahmini)",
    "gemini-2.0-flash-lite-preview-02-05": "Gemini 2.0 Flash-Lite Preview (15 RPM, 1500/gün - Tahmini)",
    "gemini-1.5-flash": "Gemini 1.5 Flash (15 RPM, 1500/gün - Tahmini)",
    "gemini-1.5-pro": "Gemini 1.5 Pro (2 RPM, 50/gün - Tahmini)",
}

DEFAULT_MODEL = "gemini-2.5-flash"  # Highest RPM typically

# Fallback limits when API fetch fails
MODEL_LIMITS_FALLBACK = {
    "gemini-2.5-flash": {"rpm": 15, "rpd": 1500},
    "gemini-2.5-pro": {"rpm": 2, "rpd": 50},
    "gemini-2.0-flash-exp": {"rpm": 10, "rpd": 1000},
    "gemini-2.0-flash-lite-preview-02-05": {"rpm": 15, "rpd": 1500},
    "gemini-1.5-flash": {"rpm": 15, "rpd": 1500},
    "gemini-1.5-pro": {"rpm": 2, "rpd": 50},
}

# Groq Models
GROQ_MODELS = {
    "llama-3.1-70b-versatile": "Llama 3.1 70B (8000 RPM, 14400/gün)",
    "llama-3.1-8b-instant": "Llama 3.1 8B Instant (30000 RPM, 14400/gün)",
    "mixtral-8x7b-32768": "Mixtral 8x7B (5000 RPM, 14400/gün)",
    "gemma2-9b-it": "Gemma 2 9B (15000 RPM, 14400/gün)",
}

DEFAULT_GROQ_MODEL = "llama-3.1-70b-versatile"

# Groq Model Limits (all have same daily limit)
GROQ_MODEL_LIMITS = {
    "llama-3.1-70b-versatile": {"rpm": 8000, "rpd": 14400},
    "llama-3.1-8b-instant": {"rpm": 30000, "rpd": 14400},
    "mixtral-8x7b-32768": {"rpm": 5000, "rpd": 14400},
    "gemma2-9b-it": {"rpm": 15000, "rpd": 14400},
}
