import scrapy
from books.items import BooksItem

class BookSpider(scrapy.Spider):
    # Where to start scraping
    name = "book"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    # Parsing the response
    #first finds all the books on the current page and then iterates over each book
    def parse(self, response):
        # Contact to display info
        """
        @url https://books.toscrape.com
        @returns items 20 20
        @returns request 1 50
        @scrapes url title price
        """
        for book in response.css("article.product_pod"):
            item = BooksItem()
            item["url"] = book.css("h3 > a::attr(href)").get()
            item["title"] = book.css("h3 > a::attr(title)").get()
            item["price"] = book.css(".price_color::text").get()
            yield item
# yields results rather than returning them. allows multiple requests and responses concurrently.

        # Page navigation
        next_page = response.css("li.next > a::attr(href)").get()
        if next_page:
            next_page_url = response.urljoin(next_page) #combine url from website with the base URL
            self.logger.info(
                f"Navigating to next page with URL {next_page_url}."
            )
            # allows the framework to make another request to the second page using the parse method again
            yield scrapy.Request(url=next_page_url, callback=self.parse)