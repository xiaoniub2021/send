# Gunicorn 配置文件
import os
import sys

# 绑定地址和端口
bind = f"0.0.0.0:{os.environ.get('PORT', '8080')}"

# Worker 配置
workers = 2
worker_class = "sync"
worker_connections = 1000
timeout = 120

# 日志配置
loglevel = "info"
errorlog = "-"
# 访问日志：Gunicorn 这里必须是文件路径字符串或 "-"（stdout）
# 之前用对象会导致启动失败（Railway 部署直接报 Invalid value for accesslog）
accesslog = "-"
access_log_format = '%(h)s - - [%(t)s] "%(r)s" %(s)s %(b)s %(D)s' 
