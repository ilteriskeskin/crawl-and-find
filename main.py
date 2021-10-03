from fastapi import FastAPI
from utils.crawler import crawler
from modals.modals import CrawlModal

app = FastAPI()


@app.post("/")
async def crawl(crawl_data: CrawlModal):
    return crawler(url=crawl_data.url, find_key=crawl_data.find_key)
