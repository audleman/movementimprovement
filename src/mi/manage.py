#!/usr/bin/env python
import os
import sys

# setup environment first
BASE_PATH = os.path.abspath(__file__)
for i in range(3):
    BASE_PATH = os.path.dirname(BASE_PATH)
sys.path.insert(0, os.path.join(BASE_PATH, 'lib'))
sys.path.insert(0, os.path.join(BASE_PATH, 'src', 'mi'))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mi.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
