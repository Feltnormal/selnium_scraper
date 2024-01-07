import requests


def send_request(session, proxy):
   try:
       response = session.get('https://open.spotify.com/', proxies={'https': f"https://8.219.97.248"})
       print(response.json())
   except:
       pass


if __name__ == "__main__":
   with open('list_proxy.txt', 'r') as file:
       proxies = file.readlines()

   with requests.Session() as session:
       for proxy in proxies:
           send_request(session, proxy)
