import requests

from os import environ

from requests.auth import HTTPBasicAuth


# Import environment vars
try:
    SETTINGS_USERNAME = environ['ROUTER_RESET_USERNAME']
    SETTINGS_PASSWORD = environ['ROUTER_RESET_PASSWORD']
    SETTINGS_IP = environ['ROUTER_RESET_IP']
except KeyError as err:
    print 'FATAL: you should set environment variables to use this python script!'
    exit(1)

# Set Basic Auth
auth = HTTPBasicAuth(SETTINGS_USERNAME, SETTINGS_PASSWORD)

# Payload to reset router
payload = {
    'action': '',
    'submit_type': 'reboot',
    'submit_button': 'index',
    'change_action': 'gozila_cgi',
    'wait_time': 30,
}

# Reset
r = requests.post('https://%s/apply.cgi' % SETTINGS_IP,
                  verify=False, auth=auth, data=payload)

# Check status code
if r.status_code == 200:
    print 'Reset done'
else:
    print 'WARNING! Something has gone wrong! (status_code=%s)' % r.status_code
