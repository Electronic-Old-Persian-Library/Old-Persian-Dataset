from scrapy import Item, Field


class ArticlePhotoItem(Item):
    name = Field()
    number = Field()
    url = Field()
    file = Field()
