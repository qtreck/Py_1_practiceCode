#import libraries 'request' and BeautifulSoup' to scarpe data 
import requests
from bs4 import BeautifulSoup

# Function to scrape news articles
def scrape_news():
    url = "https://example-news-website.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract news article headlines
    headlines = soup.find_all('h2', class_='article-headline')
    for headline in headlines:
        print("News Headline:", headline.text.strip())

# Function to scrape weather information
def scrape_weather():
    url = "https://example-weather-website.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract weather details
    temperature = soup.find('span', class_='temperature').text.strip()
    condition = soup.find('div', class_='weather-condition').text.strip()

    print("Weather Information:")
    print(f"Temperature: {temperature}")
    print(f"Condition: {condition}")

# Function to scrape tech trends
def scrape_tech_trends():
    url = "https://example-tech-trends-website.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract tech trend titles
    trend_titles = soup.find_all('h3', class_='trend-title')
    for title in trend_titles:
        print("Tech Trend:", title.text.strip())

# Function to scrape product details
def scrape_product_details():
    url = "https://example-product-website.com/product-details"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract product details
    product_name = soup.find('h1', class_='product-name').text.strip()
    price = soup.find('span', class_='product-price').text.strip()

    print("Product Details:")
    print(f"Product Name: {product_name}")
    print(f"Price: {price}")

# Run the scraper functions
print("Scraping News Articles:")
scrape_news()

print("\nScraping Weather Information:")
scrape_weather()

print("\nScraping Tech Trends:")
scrape_tech_trends()

print("\nScraping Product Details:")
scrape_product_details()
