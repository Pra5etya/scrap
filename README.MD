# Scrapy:
===
## Keunggulan:
1. Dirancang khusus untuk web scraping, sangat efisien dan cepat.
2. Mendukung crawling multi-threading secara otomatis, yang membuatnya ideal untuk scraping dalam skala besar.
3. Dilengkapi dengan fitur-fitur bawaan seperti pengelolaan request, otomatisasi penanganan cookie, dan kontrol yang lebih baik terhadap crawler.
4. Mendukung pipelines untuk memproses data setelah scraping.

## Kekurangan:
1. Kurva belajar yang lebih tinggi dibandingkan BeautifulSoup.
2. Kurang fleksibel jika Anda perlu berinteraksi dengan elemen dinamis atau AJAX (JavaScript).

# Selenium:

## Keunggulan:
1. Ideal untuk scraping situs web yang menggunakan banyak JavaScript atau elemen dinamis yang memerlukan interaksi pengguna (seperti mengklik tombol atau mengisi form).
2. Menyediakan kontrol penuh atas browser dan memungkinkan Anda untuk melihat apa yang terjadi di setiap tahap scraping.

## Kekurangan:
1. Lebih lambat dibandingkan Scrapy atau BeautifulSoup karena harus memuat seluruh halaman dan menjalankan JavaScript.
2. Konsumsi sumber daya lebih tinggi, baik dari segi memori maupun CPU.
3. Bukan solusi yang ideal untuk scraping dalam skala besar.

# BeautifulSoup:

## Keunggulan:
1. Mudah digunakan dan dipahami, cocok untuk pemula.
2. Dapat digunakan bersama dengan requests untuk mengambil dan memproses halaman HTML.
3. Sangat fleksibel dan dapat diintegrasikan dengan framework lain seperti Scrapy atau Selenium untuk keperluan tertentu.

## Kekurangan:
1. Tidak mendukung crawling atau scraping secara otomatis, Anda perlu mengelola request dan crawling secara manual.
2. Tidak bisa menangani elemen dinamis atau JavaScript dengan baik; perlu digabungkan dengan Selenium untuk tugas semacam ini.

# Rekomendasi:

1. Jika Anda membutuhkan scraping dalam skala besar dan halaman yang diambil sebagian besar statis (tidak memerlukan interaksi pengguna atau rendering JavaScript), Scrapy adalah pilihan terbaik.
2. Jika Anda perlu berinteraksi dengan elemen dinamis atau situs web yang berat JavaScript, Selenium lebih cocok.
3. Jika proyek Anda kecil, atau Anda butuh fleksibilitas dan kontrol manual, BeautifulSoup adalah pilihan yang baik, terutama jika digabungkan dengan requests atau Selenium untuk kasus tertentu.

# NOTED

## Scrapy 
Scrapy menggunakan CSS selectors atau XPath untuk mengekstrak data dari halaman web, untuk experiment bisa menggunkan **scrapy shell**.


genereate project: \
    scrapy startproject project_name


must in scrapy project
================================

generate spider: \
    scrapy genspider name_of_script url_target_link

run spider: \
    scrapy crawl name_of_spider_in_script

save data: \
1. save new row \
    scrapy crawl name_of_spider_in_script -o name.format_type (JSON, CSV, atau XML) \
    
2. overwrite data \
    scrapy crawl name_of_spider_in_script -O name.format_type (JSON, CSV, atau XML)


customize scrapy (must in scrapy project)
================================
1. scrapy shell url_target_link
2. use response for checking html / css: 
    # line code
    response.css('element') or using .get() for line code
    
    # specific element 
    response.css('h1::text').get() or something \
    for all use response.css('h1::text').getall()

    # use xpath
    response.xpath('//a/text').extract() \
    cara membacanya yakni: ambil semua elemen a yang terdapat text lalu ektraksi 


note (banned IP)
================================
1. User Agents (Fingger Point): 
    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
    (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/53736

    Scrapy/VERSION (+https://scrapy.org)

    Googlebot/2.1 (+http://www.google.com/bot.html)

    => to resolve this matter add another installer: 
    ```pip install scrapy-user-agents```
    then change DOWNLOADER_MIDDLEWARES = {
        ```
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None, 
        'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
        ```
    }

2. Rotating IP with proxy
3. Use VPN

save data (feed exporter)
================================
1. use FEEDS on setting: 
    FEEDS = {
        'data/%(name)s/%(name)s_%(time)s.csv: {'format': 'csv (etc)'}
    }

2. custom_settings = {
    'FEEDS': {'name_of_file': {'format': 'csv (etc)'}}
}

3. use bacth on setting: 
    FEEDS = {
        'data/%(name)s/%(name)s_%(time)s_batch_%(batch_id)d.csv: {
            'format': 'csv (etc)', 
            'batch_item_count': 5 or any sum parsing data
        } 
    }




LINK for learn:
================================
https://thepythonscrapyplaybook.com/