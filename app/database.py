import os

from dotenv import load_dotenv


load_dotenv()



TORTOISE_ORM = {
    "connections": {
         "default": os.getenv("DATABASE_URL")
    },
    "apps": {
        "cargo": {
            "models": [
                 "app.models", "aerich.models"
            ],
            "default_connection": "default",
        },
    },
}