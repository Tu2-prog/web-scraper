import scrapy 

class MangaSpider(scrapy.Spider):
    name = "manga_spider"
    index = 1

    start_urls = ["https://manganato.com/genre-2/220"]

    def parse(self, response):
        for books in response.css("div.genres-item-info"):
            yield{
                "title": books.css('h3 > a.genres-item-name.text-nowrap.a-h::text').get(),
                "views": books.css('span.genres-item-view::text').get().replace(',', ''),
                "chapter": books.css('a.genres-item-chap.text-nowrap.a-h::text').get(),
            }
