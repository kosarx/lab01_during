import requests  # εισαγωγή της βιβλιοθήκης


def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break


url = 'http://google.com/'  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    # html = response.text
    # more(html)

    hdrs = response.headers
    for item, value in hdrs.items():
        print(f"{item:30s} {value}")