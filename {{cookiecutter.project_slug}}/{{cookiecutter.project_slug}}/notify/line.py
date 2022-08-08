import os
import requests

# ==========================================================
# LINE Notify
# ==========================================================
def send(notification_message):
    line_notify_token = os.environ.get("LINE_NOTIFY_ACCESS_TOKEN")
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': "\n"+f'{notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)
