#!/bin/bash
# Vercel build script
pip install -r api/requirements.txt
python manage.py collectstatic --noinput
