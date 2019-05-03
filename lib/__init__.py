# coding: utf-8
import datetime

import httplib2
import lxml.html as lhtml

http = httplib2.Http()


def request_uri_doc(uri, method):
    resp, html = http.request(uri, method)
    return lhtml.document_fromstring(html)


def render_element_content(element):
    return ("" if element.text is None else element.text) + "".join(map(lambda x: lhtml.tostring(x, encoding='UTF-8'), element))


def get_datetime_utcnow():
    return datetime.datetime.utcnow()


def date_to_standart_format(date):
    return date.strftime('%a, %d %b %Y %H:%M:%S GMT')


def get_now_standart_format():
    return date_to_standart_format(get_datetime_utcnow())
