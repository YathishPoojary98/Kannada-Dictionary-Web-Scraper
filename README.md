# Kannada Dictionary Web Scraper
This project consists of a Python script and a Jupyter Notebook designed to scrape Kannada dictionary entries from the Padakanaja website. The scraped data is cleaned and organized, extracting only words and their meanings, and then saved into an Excel file for easy access and analysis.

Features:

Web Scraping: Efficiently fetches dictionary entries from the specified URL.
Data Cleaning: A Jupyter Notebook (Pada_scrape.ipynb) processes the raw text, extracting only the relevant words and their meanings.
Excel Export: The cleaned data is saved into an Excel file for convenient use and further analysis.
Multiple Page Support: Configurable to scrape multiple pages based on the specified parameters.
UTF-8 Encoding: Handles Kannada characters properly during data extraction and saving.

Requirements:

Python 3.x
requests library
BeautifulSoup from the bs4 library
pandas library for Excel export
Jupyter Notebook for the cleaning process

Installation:

Clone the Repository:

git clone https://github.com/YathishPoojary98/kannada-dictionary-scraper.git

cd kannada-dictionary-scraper

Install Required Libraries: You can install the required libraries using pip:

pip install requests beautifulsoup4 pandas

Run the Scraper Script: Ensure you have Python installed, then run the following command to scrape the dictionary:

python scraper.py

Clean the Data: 

Open Pada_scrape.ipynb in Jupyter Notebook and run the cells to clean the scraped data. This will extract only the words and their meanings.

Export to Excel: 

After cleaning the data, the notebook will save the cleaned entries to an Excel file.

Output:

The scraped raw data will be saved in scraped_data.txt.
The cleaned data will be exported to an Excel file (e.g., dictionary_entries.xlsx).

Example Usage:

Modify the script parameters as needed (base URL, page suffix, total pages).
Run the scraper script to begin scraping.
Open the Jupyter Notebook and execute the cleaning process.
Check the resulting Excel file for the organized dictionary entries.
