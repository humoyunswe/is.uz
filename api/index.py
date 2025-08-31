from vercel_python_wsgi import make_handler
from core.wsgi import application  # заменяй myproject на имя твоего Django проекта

handler = make_handler(application)
