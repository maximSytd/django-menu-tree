import os

from dotenv import dotenv_values

from .paths import BASE_DIR

config = dotenv_values(".env")

LANGUAGE_CODE = config.get("LANGUAGE_CODE", "en")

TIME_ZONE = config.get("TIME_ZONE", "UTC")

USE_I18N = True
USE_L10N = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)
