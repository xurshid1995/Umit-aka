"""Gunicorn configuration file"""
import multiprocessing
import os

# Server socket - faqat localhost (xavfsizlik uchun)
bind = os.getenv('BIND', '127.0.0.1:5000')
backlog = 2048

# Worker processes
# âœ… Optimizatsiya: 2GB RAM uchun workers kamaytirildi (5â†’3)
# Default formula: cpu_count * 2 + 1 = 5 (1 CPU da)
# Yangi: 3 worker (har biri ~70MB = 210MB)
workers = int(os.getenv('WORKERS', 3))
worker_class = 'sync'
worker_connections = 1000
timeout = int(os.getenv('TIMEOUT', 300))  # 5 minut - API requestlar uchun yetarli
keepalive = 5  # Keep-alive connection 5 sekund

# Request size limits (100MB - rasmlar uchun)
limit_request_line = 8190  # Request line length
limit_request_fields = 200  # Request header count
limit_request_field_size = 0  # No limit on header size (default 8190)

# Logging
accesslog = 'logs/access.log'
errorlog = 'logs/error.log'
loglevel = 'warning'  # info -> warning (SIGTERM loglarini yashirish uchun)
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Process naming
proc_name = 'umit_aka_app'

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# SSL
keyfile = None
certfile = None
