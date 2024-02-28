import requests
import re

# def more(text):
#     count = 0
#     for line in text.split('\n'):
#         print(line)
#         count += 1
#         if count % 30 == 0:
#             reply = input('Show more (y/n)? ')
#             if reply == 'n':
#                 break

def main():
    url = ""
    while not url:
        url = input("Enter URL:")

    if "http://" not in url or "https://" not in url: # appending info if neessary
        url = "https://" + url

    try:
        with requests.get(url) as response:  # Sending a GET request
            print("------------ HEADERS --------------")
            print("-----------------------------------")
            hdrs = response.headers
            for item, value in hdrs.items():
                print(f"{item:30s} {value}")

            print("------------ WEB SERVER -------------------------------------------------")
            print("-----------------------------------")
            server = response.headers.get('Server')
            if server:
                print(f"Server technology used: {server}")
            else:
                print("No server info found")

            print("------------ COOKIES --------------")
            print("-----------------------------------")
            cookies = response.headers.get('Set-Cookie')

            if cookies:
                cookies_list = cookies.split(', ')  # Split cookies string into individual cookies
                print("Cookies are: ", end="")
                for i in range(len(cookies_list)):
                    if i == 0: 
                        print(f"{i}. {cookies_list[i]}")
                        continue
                    print(f"             {i}. {cookies_list[i]}")
                    #print(cookie)

                print("------------ NAME OF COOKIE AND EXPIRY --------------")
                print("-----------------------------------------------------")
                print("Names:")
                pattern = re.compile(r'.*?;') # find substring from start all the way to the first ';'
                for cookie in cookies_list:
                    if cookie[0].isdigit(): # cookies_list is split on ', '. That means that "Sat, 29 March" also gets split.
                        continue # ignore this, it is part of expiry date, not name
                    match = pattern.match(cookie)
                    print(f"> {match.group()}")

                pattern = re.compile(r'(?:exp|Exp).*?;') # find substring that starts with "exp" all the way up to the first ';'
                print("And their expiry:")
                matches = pattern.findall(cookies) # find ALL such occurences
                if matches:
                    for match in matches:
                        print(f"> {match}")

            else:
                print("No cookies found")
    except requests.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")

if __name__ == "__main__":
    main()