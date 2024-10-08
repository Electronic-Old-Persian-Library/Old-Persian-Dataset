from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline

from scraper.items import ArticlePhotoItem, LinkedPhotoItem


class DownloadArticlePhotoPipeline(FilesPipeline):
    def file_path(
        self,
        request,
        response=None,
        info=None,
        *,
        item: ArticlePhotoItem | None = None,
    ) -> str:
        if not item:
            raise DropItem()

        return f"{item['name']}_{item['number']}.jpg"


class DownloadLinkedPhotoPipeline(FilesPipeline):
    def file_path(
        self,
        request,
        response=None,
        info=None,
        *,
        item: LinkedPhotoItem | None = None,
    ) -> str:
        if not item:
            raise DropItem()

        return f"{item['name']}_{item['number']}_linked.jpg"
