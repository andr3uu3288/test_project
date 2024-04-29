import requests
from bs4 import BeautifulSoup
import certifi
import requests

response = requests.get('https://skyscanner.com', verify=certifi.where())


def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    headlines = soup.find_all('h1')  # Adjust the tag to your needs
    for idx, headline in enumerate(headlines):
        print(f"Headline {idx + 1}: {headline.get_text(strip=True)}")

def main():
    url = 'https://skyscanner.com'  # Replace with the URL of the site you want to crawl
    html = fetch_page(url)
    if html:
        parse_html(html)

if __name__ == "__main__":
    main()
