import schedule
import time
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from sampling.spiders.books_scrape import CrawlingSpider  # Sesuaikan dengan struktur proyek Anda

def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(CrawlingSpider)
    process.start()

# Jadwalkan spider untuk berjalan setiap hari pada pukul 02:00
schedule.every().day.at("02:00").do(run_spider)

# Menjaga script berjalan untuk mempertahankan penjadwalan
while True:
    schedule.run_pending()
    time.sleep(1)
