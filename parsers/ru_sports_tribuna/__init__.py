# coding=utf-8
from urllib.parse import urljoin

from lib import render_element_text, render_element_clean


def get_common_info():
    return {
        'title': 'Sports.Ru: «Трибуна» – лучшее.',
        'lang': 'ru-RU',
        'image': 'http://www.sports.ru/i/logo_rss.gif',
        'description': 'Sports.Ru: «Трибуна» – это крупнейшее русскоязычное сообщество спортивных болельщиков, '
                       'первое социальное медиа о спорте, которое создают сами пользователи.',
        'copyright': '1998–2011 © Sports.ru'
    }


def parse(link, doc):
    posts = []
    post_list = doc.xpath('//*[contains(@class, "blog-post-list")]/*[@data-materialid]')

    if len(post_list) > 0:
        for post_node in post_list:
            h2 = post_node.xpath('h2')[0]
            lnk = h2.xpath('.//a[@href]')[-1]
            h2.drop_tree()
            url = urljoin(link, lnk.attrib['href'])

            post = {
                'title': render_element_text(h2),
                'link': url,
                'guid': url,
            }

            info_node = post_node.xpath('div[position() = 1]')

            if len(info_node) > 0:
                info = info_node[0]
                info.drop_tree()

                pub_date_value = None
                try:
                    pub_date = info.xpath('time[@datetime]')[0]
                    pub_date.drop_tree()
                    pub_date_value = pub_date.attrib['datetime']
                except Exception:
                    pass

                author = None
                try:
                    author = info.xpath('.//*[@class="bold"]/a[@href]')[0]
                    author.drop_tree()
                except Exception:
                    pass

                if pub_date_value:
                    post['pubDate'] = render_element_text(pub_date_value)

                if author:
                    post['author'] = render_element_text(author)

            comments_url = None
            try:
                comments = post_node.xpath('.//*[@class="links-line"]/a[@href]')[0]
                comments.drop_tree()
                comments_url = urljoin(link, comments.attrib['href'])
            except Exception:
                pass

            if comments_url:
                post['comments'] = comments_url

            post['description'] = render_element_clean(post_node)
            posts.append(post)

    return [posts, get_common_info()]
