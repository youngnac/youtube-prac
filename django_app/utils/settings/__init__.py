import json
import os


def search_conf():
    base = os.path.abspath(__file__)
    util = os.path.dirname(os.path.dirname(base))
    conf = os.path.join(os.path.dirname(os.path.dirname(util)), '.conf')
    setting_local = os.path.join(conf, 'settings_local.json')
    read = json.loads(open(setting_local).read())
    return read
