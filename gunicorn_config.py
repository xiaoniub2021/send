import os

bind = f"0.0.0.0:{os.environ.get('PORT', '8080')}"

workers = 1                  # eventlet 建议 1 个 worker
worker_class = "eventlet"    # 必须是这个
worker_connections = 1000    # 每 worker 支持连接数

timeout = 120

loglevel = "info"
errorlog = "-"
accesslog = "-"
access_log_format = '%(h)s - - [%(t)s] "%(r)s" %(s)s %(b)s %(D)s'
