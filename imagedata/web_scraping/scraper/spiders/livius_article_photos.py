from typing import Iterable

import scrapy
from scrapy.http import HtmlResponse, Request

from scraper.items import ArticlePhotoItem


class LiviusSpider(scrapy.Spider):
    name = "livius_article_photos"

    inscriptions_image_urls: list[tuple[str, str]] = []
    base_url = "https://www.livius.org"

    custom_settings = {
        "ITEM_PIPELINES": {
            "scraper.pipelines.DownloadArticlePhotoPipeline": 1,
        },
    }

    def start_requests(self) -> Iterable[Request]:
        url = "https://www.livius.org/sources/content/achaemenid-royal-inscriptions/"

        yield Request(url=url, callback=self.parse)

    def parse(self, response: HtmlResponse) -> Iterable[Request]:
        self.log("Extracting Inscriptions names and urls")
        names_urls = self._get_inscriptions_urls(response)
        self.log(f"Found {len(names_urls)} Inscriptions urls")

        for name, url in names_urls:
            self.log(f"{name} {url}")
            yield Request(url, self.parse_inscription_page, cb_kwargs={"name": name})

    def _get_inscriptions_urls(self, response: HtmlResponse) -> list[tuple[str, str]]:
        urls: list[tuple[str, str]] = []

        inscriptions = response.xpath('//*[@id="content"]/table[2]/tbody/tr/td[1]/a')
        for inscription in inscriptions:
            url = inscription.attrib["href"]
            if not url.startswith(self.base_url):
                url = self.base_url + url
            name = inscription.xpath("text()").get()
            urls.append((name, url))

        self.log("Done")

        return urls

    def parse_inscription_page(
        self,
        response: HtmlResponse,
        name: str,
    ) -> Iterable[Request]:
        article_photos_urls = self._get_article_photos_urls(response)
        self.log(f"Found {len(article_photos_urls)} photo(s) in {response.url}")

        for number, url in enumerate(article_photos_urls):
            self.log(f"{name}, {number}, {url}")
            yield ArticlePhotoItem({"name": name, "url": [url], "number": number})

    def _get_article_photos_urls(self, response: HtmlResponse) -> list[str]:
        photos_urls = []
        for img in response.xpath("/html/body/section/article//img"):
            dad = img.xpath("../*").get()
            grandpa = img.xpath("../../*").get()

            url = img.attrib["src"]
            if not url.startswith(self.base_url):
                url = self.base_url + url

            if dad.startswith("<a") or grandpa.startswith("<a"):
                self.log(
                    f"Ignore linked photo: article: {response.url}, photo url: {url}"
                )
                continue

            photos_urls.append(url)

        return photos_urls
