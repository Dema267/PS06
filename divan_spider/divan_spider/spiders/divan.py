import scrapy


class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru/category/svet"]

    def parse(self, response):

       # Создаём переменную, в которую будет сохраняться информация
       svets = response.css('div._Ud0k')
       # Настраиваем работу с каждым отдельным диваном в списке
       for svet in svets:
           # Используем новый для нас оператор "yield", который помогает обрабатывать одно отдельное действие
           yield {
           'name' : svet.css('div.lsooF span::text').get(),
           'price' : svet.css('div.pY3d2 span::text').get(),
           'url' : svet.css('a').attrib['href']
           }
