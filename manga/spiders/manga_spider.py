from urllib import response
import scrapy
from ..items import MangaItem

class MangaSpider(scrapy.Spider):
    name = "manga_spider"
    index = 1

    start_urls = ["https://manganato.com/genre-2/"]

    def parse(self, response):
        all_div_books = response.css("div.genres-item-info")
        item = MangaItem()
        for books in all_div_books:
            title = books.css('h3 > a.genres-item-name.text-nowrap.a-h::text').get()
            views = books.css('span.genres-item-view::text').get().replace(',', '')
            chapter = books.css('a.genres-item-chap.text-nowrap.a-h::text').get()
            item['title'] = title
            item['views'] = views
            item['chapter'] = chapter

            yield item 
        next_page = f'https://manganato.com/genre-2/'+str(MangaSpider.index)+''

        if MangaSpider.index <= 311:
            MangaSpider.index += 1
            yield response.follow(next_page, callback = self.parse)

