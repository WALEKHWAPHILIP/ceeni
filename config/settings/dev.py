# Import all base settings to extend and override where needed
from .base import *

# Load environment variables from a .env file into the system environment
from dotenv import load_dotenv
load_dotenv()

# Enable debug mode — only recommended for development environments
DEBUG = True

# Allow connections from any host (not recommended for production)
ALLOWED_HOSTS = ["*"]

# Configure the default database using PostgreSQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",  # Use PostgreSQL backend
        "NAME": os.getenv("DB_NAME"),                # Database name from environment
        "USER": os.getenv("DB_USER"),                # Database user from environment
        "PASSWORD": os.getenv("DB_PASSWORD"),        # Password from environment
        "HOST": "localhost",                         # Database host (localhost here)
        "PORT": "5432",                              # Default PostgreSQL port
    }
}
