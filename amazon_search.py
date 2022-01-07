from autoscraper import AutoScraper

amazon_url='https://www.amazon.com.br/s?k=iphone'

wanted_lst=['Apple iPhone 12 (64 GB) - Preto', 'R$5.599,90']

scraper=AutoScraper()

scraped_things=scraper.build(amazon_url,wanted_lst)

print(scraped_things)