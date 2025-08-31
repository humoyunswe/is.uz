import os
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Import Django and create application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# For Vercel
def handler(request, context):
    return application(request, context)
