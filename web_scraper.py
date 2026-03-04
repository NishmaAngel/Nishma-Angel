import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    """
    A simple web scraper using requests and BeautifulSoup 
    to extract quotes from http://quotes.toscrape.com/
    
    Note: You may need to install the following packages:
    pip install requests beautifulsoup4
    """
    url = "http://quotes.toscrape.com/"
    print(f"Fetching data from {url}...\n")
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all quote elements
    quotes = soup.find_all('div', class_='quote')
    
    print("--- Top Quotes from Quotes to Scrape ---")
    for i, quote in enumerate(quotes, 1):
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        print(f"{i}. {text}\n   - {author}\n")

if __name__ == "__main__":
    scrape_quotes()
