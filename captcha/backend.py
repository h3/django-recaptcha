import requests

URL = 'https://www.google.com/recaptcha/api/siteverify'


def verify_challenge(token):
    rs = requests.get(URL)
    return rs.json()
