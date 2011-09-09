# coding: utf-8
import sys, os
from bottle import response, route, debug, default_app
from parse import get_feed_parser_by_id

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

@route('/id:id#[0-9]+#')
def generate_feed(id):
	response.content_type = 'text/xml; charset=utf-8'
	return get_feed_parser_by_id(int(id)).generate()

debug(True)
application = default_app()