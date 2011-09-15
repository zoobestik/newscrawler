# coding: utf-8
import sys, os
from bottle import response, route, debug, default_app, template
from parse import get_feed_parser_by_id
from lib.config import get_config_data

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

@route('/:is_page_exist#(index\.html)?#', template='index')
def index(is_page_exist):
	urls = get_config_data()['urls']
	return dict(urls=urls, )

@route('/id:id#[0-9]+#')
def generate_feed(id):
	response.content_type = 'text/xml; charset=utf-8'
	return get_feed_parser_by_id(int(id)).generate()

debug(True)
application = default_app()