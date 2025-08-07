# webscraper
Web Scraper for News Headlines. Objective: Scrape top headlines from a news website. Tools : Python, requests, BeautifulSoup Deliverables: Python script + .txt file of headlines Hints/Mini Guide: 1.Use requests to fetch HTML 2.Use BeautifulSoup to parse tags 3.Save the titles in a .txt file Outcome: : Automate data collection from a public website
# 📰 Web Scraper for News Headlines

This Python script scrapes the latest news headlines from the front page of **BBC News**. It uses the `requests` library to fetch web content and `BeautifulSoup` to parse the HTML and extract relevant information. The scraped headlines are then saved into a clean, timestamped text file.
---
## ✨ Features
* **Automated Data Collection**: Fetches data without manual intervention.
* **HTML Parsing**: Uses BeautifulSoup to accurately target and extract headline text.
* **Clean Output**: Saves the headlines in a formatted and easy-to-read `.txt` file.
* **Error Handling**: Includes basic checks for network errors.
* **Responsible Scraping**: Mimics a real browser by setting a `User-Agent` header.
---
## 📋 Requirements
You need to have Python 3 installed. Additionally, you'll need the following two libraries:
* `requests`
* `beautifulsoup4`
You can install them using pip:
```bash
pip install requests beautifulsoup4
