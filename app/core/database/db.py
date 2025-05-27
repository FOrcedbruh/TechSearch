from app.core import Settings

settings = Settings()

database_config = {
    "connections": {
        "default": settings.db.url,
    },
    "apps": {
        "models": {
            "models": ["aerich.models"] + settings.db.models,
            "default_connection": "default",
        }
    }
}