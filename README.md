# Webscraping

virtual environment 
python -m venv venv
venv\Scripts\Activate
 pip install scrapy
 pip show scrapy
python -m scrapy startproject books

Run spider manually  Interactive scraping console
python -m scrapy shell http://books.toscrape.com

# Selecting elements from html after inspecting 
>>> all_book_elements = response.css("article.product_pod")
>>> for book in all_book_elements:
...     print(book.css("h3 > a::attr(title)").get())

creating the spider 
exit()
cd books
 Generate new spider using pre-defined templates
python -m scrapy genspider book https://books.toscrape.com/

Running the spider
python -m scrapy crawl book

python -m pip install pymongo