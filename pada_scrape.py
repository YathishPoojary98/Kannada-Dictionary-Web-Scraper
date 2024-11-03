import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://padakanaja.karnataka.gov.in/open_dictionary/%e0%b2%95%e0%b2%a8%e0%b3%8d%e0%b2%a8%e0%b2%a1%20%e0%b2%ae%e0%b2%a4%e0%b3%8d%e0%b2%a4%e0%b3%81%20%e0%b2%b8%e0%b2%82%e0%b2%b8%e0%b3%8d%e0%b2%95%e0%b3%83%e0%b2%a4%e0%b2%bf%20%e0%b2%87%e0%b2%b2%e0%b2%be%e0%b2%96%e0%b3%86/"
page_suffix = "48/200"  # Start from the first page
total_pages = 5  # Set the number of pages you want to scrape

# Open a file for writing
with open('scraped_data.txt', 'w', encoding='utf-8') as file:
    for i in range(total_pages):
        url = urljoin(base_url, f"{page_suffix}/{i*200}")
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract text content from the page
            scraped_data = soup.get_text()

            # Write the data to the file
            file.write(scraped_data)

            print(f"Scraping page {i + 1}")
        else:
            print(f"Failed to fetch page {i + 1}")
