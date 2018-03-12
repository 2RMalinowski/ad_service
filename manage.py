#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ad_service.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ui_app.settings")
>>>>>>> 2a4ab3107b197b6efa4489ff41b7551b7f6cc485
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
