from app.application import create_app
import uvicorn
from app.core import Settings

settings = Settings()

app = create_app()


if __name__ == "__main__":
    uvicorn.run(app=app, host=settings.app.host, port=settings.app.port)
