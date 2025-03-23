# Web Scraping with Scrapy

This guide provides step-by-step instructions on setting up a virtual environment, installing Scrapy, creating a web scraper, and running the spider to extract book data from `books.toscrape.com`.

## Prerequisites
Make sure you have **Python** installed on your system (Python 3.x recommended).

## Setting Up the Virtual Environment
Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\Activate  # On Windows
source venv/bin/activate  # On Mac/Linux
```

## Installing Scrapy
Install Scrapy using pip:
```bash
pip install scrapy
pip show scrapy  # To verify the installation
```

## Creating a Scrapy Project
Initialize a new Scrapy project named books:
```bash
python -m scrapy startproject books
```

## Running the Scrapy Shell
To manually test scraping and inspect elements:
```bash
python -m scrapy shell http://books.toscrape.com
```

### Selecting Elements from HTML
After inspecting elements using browser dev tools, extract book titles:
```python
all_book_elements = response.css("article.product_pod")
for book in all_book_elements:
    print(book.css("h3 > a::attr(title)").get())
```

## Creating a New Spider
Exit the Scrapy shell and navigate to the project directory:
```bash
exit()
cd books
```
Generate a new spider using a predefined template:
```bash
python -m scrapy genspider book https://books.toscrape.com/
```

## Running the Spider
Run the spider to start scraping:
```bash
python -m scrapy crawl book
```

## Installing MongoDB Support
To store scraped data in MongoDB, install `pymongo`:
```bash
python -m pip install pymongo
```

## Additional Notes
- Make sure to inspect the website structure before scraping.
- Use Scrapy’s logging and debugging features to troubleshoot issues.
- Store the scraped data in structured formats like JSON, CSV, or databases.

---
This project provides a basic introduction to web scraping using Scrapy and how you can extend this project by integrating databases such as MongoDB for data storage or applying data analysis techniques on the scraped data.

