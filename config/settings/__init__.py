import os

# Get the current environment from the environment variable 'DJANGO_ENV'
# Defaults to 'dev' (development) if not set
env = os.getenv("DJANGO_ENV", "dev")

# Conditionally import settings based on the environment
if env == "prod":
    # In production, import all settings from prod.py
    from .prod import *
else:
    # In any other environment (default to development), import dev.py settings
    from .dev import *
