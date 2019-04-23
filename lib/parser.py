import importlib

from lib import get_now_standart_format, request_uri_doc
from lib.config import get_url_data_by_id


def update_common_info(link, common_info):
    now = get_now_standart_format()

    common_info.setdefault('link', link)
    common_info.setdefault('last_build_date', now)
    common_info.setdefault('pub_date', now)

    return common_info


def generate(link, parser):
    doc = request_uri_doc(link)

    posts, common_info = parser(link, doc)

    if not common_info:
        common_info = {}

    common_info = update_common_info(link, common_info)

    info = common_info.copy()

    info.update({
        'items': posts,
    })

    return info


def generate_feed_by_id(id):
    config_url = get_url_data_by_id(id)
    link = config_url['url']

    pkg_name = config_url['parser']
    pkg = importlib.import_module('parsers.' + pkg_name)

    feed = generate(link, pkg.parse)
    feed.setdefault('parser', pkg_name)

    return feed
