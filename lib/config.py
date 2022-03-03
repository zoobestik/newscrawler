# coding: utf-8
from yaml import safe_load

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

with open("config.yaml", 'r') as stream:
    config_data = safe_load(stream)


def get_config_data():
    return config_data


def get_url_data_by_id(id):
    return get_config_data()['urls'][id]
