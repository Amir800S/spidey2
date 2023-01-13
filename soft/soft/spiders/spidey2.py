import scrapy


class Spidey2Spider(scrapy.Spider):
    name = 'spidey2'
    allowed_domains = ['3dnews.ru']
    start_urls = ['http://3dnews.ru/news']  # Страница для сбора данных

    def parse(self, response):
        """ Фукнция парсинга """
        link = response.xpath('.//div[@class="cntPrevWrapper"]/a/@href').getall()
        title = response.xpath('.//h1/text()').getall()
        desc = response.xpath('.//p/text()').getall()
        date = response.css("span.entry-date::text").extract()

        row_data = zip(link, title, desc, date)  # Создания итерируемого кортежа
        for post in row_data:
            # Словарь для хранения данных
            scraped_data = {
                'Link': f'3dnews.ru{post[0]}',  # Колонки для CSV файла
                'Title': post[1],
                'Description': post[2],
                'Date': post[3],
            }
            yield scraped_data
