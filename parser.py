from bs4 import BeautifulSoup as BS
from loguru import logger
import requests as req

def get_domain(url):
    raw_domain = url.strip('htpps://')
    domain = raw_domain[:raw_domain.find('/')]
    logger.info(domain)
    return domain

def parse_photo_urls(url):
    resp = req.get(url)
    soup = BS(resp.text, 'html.parser') 
    
    if get_domain(url) == 'fonwall.ru':
        div = soup.find('div', class_='photos')
        articles = div.find_all('article')
        for article in articles:
            a = article.find('a', class_='js-photo-link')

            logger.success(a['href'])
            


parse_photo_urls('https://fonwall.ru/search?q=танк')
