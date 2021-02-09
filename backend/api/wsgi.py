import os

bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8080')
workers = os.environ.get('GUNICORN_WORKERS', '1')
reload = os.environ.get('GUNICORN_RELOAD', False)
loglevel = os.environ.get('GUNICORN_LOGLEVEL', 'info')
timeout = os.environ.get('GUNICORN_TIMEOUT', 30)
graceful_timeout = os.environ.get('GUNICORN_GRACEFUL_TIMEOUT', 30)
