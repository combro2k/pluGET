# Handles the web requests
import requests


def doAPIRequest(url):
    headers = {'user-agent': 'pluGET/1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code != 404:
        packageDetails = response.json()
    else:
        packageDetails = None

    return packageDetails
