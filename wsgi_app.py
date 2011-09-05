# coding: utf-8
import bottle, datetime, httplib2
from urlparse import urljoin
from bottle import view, response, route, error, template
import lxml.html as lhtml

def render(element):
	return element.text + "".join(map (lambda x: lhtml.tostring(x, encoding='UTF-8'), element))

@route('/sports.ru/tribuna/automoto/')
def generate_feed():
	link, items = 'http://www.sports.ru/tribuna/automoto/', []
	resp, html = http.request(link, 'GET')

	now = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
	response.content_type = 'text/xml; charset=utf-8' 
	soup = lhtml.document_fromstring(html)
	posts = soup.xpath('//div[@class="blog-content"]')

	for post in posts:
		h2  = post.xpath('h2')[0]
		lnk = h2.xpath('.//a')[0]
		h2.drop_tree()
		url = urljoin(link, lnk.attrib['href'])
		items.append({
			'title': render(lnk).strip(),
			'link': url,
			'guid': url,
			'description':  render(post)
		})

	return template('rss2.0', template_settings=dict(noescape=True), **(dict(title='Sports.Ru: «Трибуна» – лучшее.', 
			link=link, lang='ru-RU', description='Sports.Ru: «Трибуна» – это крупнейшее русскоязычное сообщество спортивных болельщиков, первое социальное медиа о спорте, которое создают сами пользователи.',
			last_build_date=now, pub_date=now, items=items,
			copyright='1998–2011 © Sports.ru')))


http = httplib2.Http()
application = bottle.default_app()