# coding: utf-8
import datetime

import httplib2
import lxml.html as lhtml
from lxml.html.clean import clean_html, Cleaner

http = httplib2.Http()
cleaner = Cleaner(scripts=True, style=True, links=True, frames=True, forms=True, safe_attrs_only=True)

def request_uri_doc(uri, method):
    resp, html = http.request(uri, method)
    return lhtml.document_fromstring(html)


def render_element_text(element):
    return element.text_content() if hasattr(element, 'text_content') else ""


def render_element_clean(element):
    return lhtml.tostring(cleaner.clean_html(element), encoding='UTF-8')


def get_datetime_utcnow():
    return datetime.datetime.utcnow()


def date_to_standart_format(date):
    return date.strftime('%a, %d %b %Y %H:%M:%S GMT')


def get_now_standart_format():
    return date_to_standart_format(get_datetime_utcnow())
