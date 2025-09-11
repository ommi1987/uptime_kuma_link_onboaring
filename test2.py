from uptime_kuma_api import UptimeKumaApi
import time
URL='http://192.168.101.13:3001//dashboard'
with UptimeKumaApi(URL) as api:
  api.login(values.username, values.password)
  api.add_monitor(type='ping', name=col2[row].value, hostname=col1[row].value)
