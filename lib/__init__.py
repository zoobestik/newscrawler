# coding: utf-8
import datetime, httplib2, lxml.html as lhtml

http = httplib2.Http()

def get_uri_soup(uri):
    resp, html = http.request(uri, 'GET')
    return lhtml.document_fromstring(html)

def render_element_content(element):
    return element.text + "".join(map (lambda x: lhtml.tostring(x, encoding='UTF-8'), element))


def get_datetime_utcnow():
    return datetime.datetime.utcnow()

def date_to_standart_format(date):
    return date.strftime('%a, %d %b %Y %H:%M:%S GMT')

def get_now_standart_format():
    return date_to_standart_format(get_datetime_utcnow())