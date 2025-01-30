# 📖 Kannada Dictionary Web Scraper

This project consists of a **Python script** and a **Jupyter Notebook** designed to **scrape Kannada dictionary entries** from the **Padakanaja website**. The scraped data is **cleaned and organized**, extracting only words and their meanings, and then saved into an **Excel file** for easy access and analysis.

---

## 🚀 Features

✅ **Web Scraping** – Efficiently fetches dictionary entries from the specified URL.  
✅ **Data Cleaning** – A Jupyter Notebook (`Pada_scrape.ipynb`) processes the raw text, extracting only relevant words and their meanings.  
✅ **Excel Export** – The cleaned data is saved into an **Excel file** for convenient use and further analysis.  
✅ **Multiple Page Support** – Configurable to scrape multiple pages based on the specified parameters.  
✅ **UTF-8 Encoding** – Handles **Kannada characters** properly during data extraction and saving.  

---

## 🛠 Requirements

Ensure you have the following installed before running the script:

- **Python 3.x**
- **requests** library
- **BeautifulSoup** from the `bs4` library
- **pandas** library for Excel export
- **Jupyter Notebook** for data cleaning

---

## 📥 Installation

### 1️⃣ Clone the Repository

To get started, clone the repository using:

```bash
git clone https://github.com/YathishPoojary98/kannada-dictionary-scraper.git
```
Navigate into the cloned directory:

```bash
cd kannada-dictionary-scraper
```
2️⃣ Install Required Libraries
Install the necessary dependencies using pip:

```bash
pip install requests beautifulsoup4 pandas
```
📌 Usage
1️⃣ Run the Scraper Script
Ensure you have Python installed, then execute the following command to scrape the dictionary:

```bash
python scraper.py
```
This will fetch Kannada dictionary entries from the Padakanaja website.

2️⃣ Clean the Data
After scraping, open the Jupyter Notebook (Pada_scrape.ipynb) and run the cells to clean the scraped data.
The script extracts only the words and their meanings.

3️⃣ Export to Excel
Once cleaned, the notebook will save the organized dictionary entries to an Excel file.

## 📂 Output

| File Name                 | Description                                  |
|---------------------------|----------------------------------------------|
| `scraped_data.txt`        | Raw scraped dictionary entries.              |
| `dictionary_entries.xlsx` | Cleaned and structured data in an Excel file. |

🎯 Example Usage
Modify script parameters as needed (e.g., base URL, page suffix, total pages).
Run the scraper script to begin scraping.
Open the Jupyter Notebook and execute the data cleaning process.
Check the resulting Excel file for the structured dictionary entries.
