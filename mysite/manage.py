#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    """
    Designating the settings

    DJANGO_SETTINGS_MODULE
    When you use Django, you have to tell it which settings you're using.
    Do this by using an environment variable, DJANGO_SETTINGS_MODULE.

    The value of DJANGO_SETTINGS_MODULE should be in Python path syntax,
    e.g. mysite.settings. Note that the settings module should be on the
    Python import search path.
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
