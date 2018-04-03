import json
import os
import sys

from bson.json_util import dumps

sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
import mongodb_client  # pylint: disable=import-error

def get_one_news():
    """Get one news"""
    res = mongodb_client.get_db()['news'].find_one()
    return json.loads(dumps(res))
