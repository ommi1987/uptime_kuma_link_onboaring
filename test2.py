from uptime_kuma_api import UptimeKumaApi
import time
import os
import sys

github_user = os.getenv("GITHUB_USER")
github_pass = os.getenv("GITHUB_PASS")

name = sys.argv[1]
hostname = sys.argv[2]

URL='http://192.168.101.13:3001//dashboard'
with UptimeKumaApi(URL) as api:
  api.login(github_user, github_pass)
  notifications = api.get_notifications()
  # Find the one you want (by name or other property)
  webhook_name = "Uptime Kuma ISP Alert"  # existing webhook name
  notif_id = None
  for n in notifications:
    if n["name"] == webhook_name:
        notif_id = n["id"]
        break    
  api.add_monitor(type='ping', name=name, hostname=hostname, notificationIDList=notif_id)
