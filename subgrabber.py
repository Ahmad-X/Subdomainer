import requests
#Coded by Ahmad-X
def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
          pass

target_url = input("[+] Enter Target Url -->  ")

try:
     while True:
         with open("Subdomain.txt", "r") as wordlist_file:
             for line in wordlist_file:
                 word = line.strip()
                 test_url = word + "." + target_url
                 response = request(test_url)
                 if response:
                     print("\033[31m[+] Discoverd Subdomain --> " + test_url)
                 else:
                     pass
except KeyboardInterrupt:
    print('\n\x1b[93;41m[+] CTRL + C detected ... <3')
    print ("\033[39m")
