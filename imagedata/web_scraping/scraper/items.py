from scrapy import Item, Field


class ArticlePhotoItem(Item):
    name = Field()
    number = Field()
    url = Field()
    file = Field()


class LinkedPhotoItem(Item):
    name = Field()
    number = Field()
    url = Field()
    file = Field()
