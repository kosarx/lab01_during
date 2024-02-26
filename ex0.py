import requests  # εισαγωγή της βιβλιοθήκης
import re

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break


url = 'http://facebook.com/'  # προσδιορισμός του url

#if not url has http... TODO

with requests.get(url) as response:  # το αντικείμενο response
    # html = response.text
    # more(html)

    hdrs = response.headers
    for item, value in hdrs.items():
        print(f"{item:30s} {value}")

    print("--------")
    cookies = response.headers.get("Set-Cookie")

    if cookies:
        print(f"Cookies are {cookies}")
    else:
        print("No cookies found")