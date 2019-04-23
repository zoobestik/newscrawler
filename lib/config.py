# coding: utf-8
from yaml import load

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

config_data = load(file('config.yaml', 'r'))


def get_config_data():
    return config_data


def get_url_data_by_id(id):
    return get_config_data()['urls'][id]
