import shodan
import os

SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
shodan_api = shodan.Shodan(SHODAN_API_KEY)

def search_shodan(query):
    results = shodan_api.search(query)
    for result in results['matches']:
        print(f"IP: {result['ip_str']} - Port: {result['port']} - {result['data']}")

search_shodan("webcam")
