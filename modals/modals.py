from pydantic import BaseModel


class CrawlModal(BaseModel):
    url: str
    find_key: str
