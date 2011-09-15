# coding: utf-8

from bottle   import template
from urlparse import urljoin

from lib import render_element_content as render_element, get_uri_soup, get_now_standart_format
from lib.config import get_url_data_by_id
from lib.decorator import constant

class PageParser():
    def __init__(self, link, feed_info=None):
        self.link  = link
        self.feed_info = feed_info
        now = get_now_standart_format()
        self.common_info = {
            'link': self.link,
            'last_build_date': now,
            'pub_date': now
        }

        self.load()

    def get_posts(self, soup):
        return []

    def get_common_info(self, soup):
        return {}

    def load(self):
        self.soup  = get_uri_soup(self.link)
        self.posts = self.get_posts(self.soup)
        self.common_info.update(self.get_common_info(self.soup))

    def generate(self):
        info = self.common_info.copy()

        if self.feed_info:
            info.update(self.feed_info)

        info['items'] = self.posts
        out = template('rss2.0', template_settings=dict(noescape=True), **(info))
        return out 

class RuSportsTribuna(PageParser):

    def get_common_info(self, soup):
        now = get_now_standart_format()
        return {
                'title':'Sports.Ru: «Трибуна» – лучшее.',
                'lang': 'ru-RU',
                'description': 'Sports.Ru: «Трибуна» – это крупнейшее русскоязычное сообщество спортивных болельщиков, первое социальное медиа о спорте, которое создают сами пользователи.',
                'copyright': '1998–2011 © Sports.ru'
        }

    def get_posts(self, soup):
        items = []
        posts = soup.xpath('//div[@class="blog-content"]')
        for post in posts:
            h2  = post.xpath('h2')[0]
            lnk = h2.xpath('.//a')[0]
            h2.drop_tree()
            url = urljoin(self.link, lnk.attrib['href'])
            items.append({
                          'title': render_element(lnk).strip(),
                          'link': url,
                          'guid': url,
                          'description':  render_element(post)
            })
        return items

def get_feed_parser_by_id(id):
    config_url = get_url_data_by_id(id)
    return RuSportsTribuna(config_url['url'])