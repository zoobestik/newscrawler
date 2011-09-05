# coding: utf-8
import bottle, urllib2, datetime
from BeautifulSoup import BeautifulSoup
from urlparse import urljoin
from bottle import view, response, route, error, template

@route('/feed/sports.ru/tribuna/automoto/')
def generate_feed():
	link, items = 'http://www.sports.ru/tribuna/automoto/', []
	html = urllib2.urlopen(link).read()

	now = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
	response.content_type = 'text/xml; charset=utf-8'
	soup = BeautifulSoup(html)
	posts = soup.findAll('div', attrs={'class' : 'blog-content'})

	for post in posts:
		lnk = post.find('h2').extract().find('a')
		url = urljoin(link, lnk['href'])
		items.append({
			'title': lnk.renderContents(),
			'link': url,
			'guid': url,
			'description': post.prettify()
		})

	return template('rss2.0', template_settings=dict(noescape=True), **(dict(title='Sports.Ru: «Трибуна» – лучшее.', 
			link=link, lang='ru-RU', description='Sports.Ru: «Трибуна» – это крупнейшее русскоязычное сообщество спортивных болельщиков, первое социальное медиа о спорте, которое создают сами пользователи.',
			last_build_date=now, pub_date=now, items=items,
			copyright='1998–2011 © Sports.ru')))

application = bottle.default_app()