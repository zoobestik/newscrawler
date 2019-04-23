# coding: utf-8
import os
import sys

from bottle import response, route, debug, default_app, template

from lib.config import get_config_data
from lib.parser import generate_feed_by_id

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


@route('/:is_page_exist#(index\.html?)?#', template='index')
def index(is_page_exist):
    urls = get_config_data()['urls']
    return dict(urls=urls, )


@route('/feeds/:id#[0-9]+#.rss')
def generate_feed(id):
    response.content_type = 'application/rss+xml; charset=utf-8'
    feed = generate_feed_by_id(int(id))
    return template('rss2', template_settings=dict(noescape=True), **feed)


# debug(True)
application = default_app()

# generate_feed_by_id(int(1))