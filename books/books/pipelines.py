# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
#itemadapter wraps different data containers to handle them in a uniform manner
from itemadapter import ItemAdapter
import hashlib
from scrapy.exceptions import DropItem


class BooksPipeline:
    def process_item(self, item, spider):
        return item

class MongoPipeline:
    COLLECTION_NAME = "books"

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DB"),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.db[self.COLLECTION_NAME].create_index("url", unique=True)  # Enforce uniqueness

    def close_spider(self, spider):
        self.client.close()

    # removing duplicates
    def process_item(self, item, spider):
        if self.db[self.COLLECTION_NAME].find_one({"url": item["url"]}):
            raise DropItem(f"Duplicate item found: {item['url']}")
        else:
            self.db[self.COLLECTION_NAME].insert_one(ItemAdapter(item).asdict())
            return item

    # TO update existing with latest datat
    # def process_item(self, item, spider):
    #     self.db[self.COLLECTION_NAME].update_one(
    #         {"url": item["url"]},  # Find existing item by URL
    #         {"$set": item},  # Update its fields
    #         upsert=True  # Insert if not found
    #     )
    #     return item

    def compute_item_id(self, item):
        url = item["url"]
        return hashlib.sha256(url.encode("utf-8")).hexdigest()