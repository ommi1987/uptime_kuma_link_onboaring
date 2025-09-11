from uptime_kuma_api import UptimeKumaApi
import time
import os

github_user = os.getenv("GITHUB_USER")
github_pass = os.getenv("GITHUB_PASS")

URL='http://192.168.101.13:3001//dashboard'
with UptimeKumaApi(URL) as api:
  api.login(github_user, github_pass)
  api.add_monitor(type='ping', name=col2[row].value, hostname=col1[row].value)
