import json

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        elif isinstance(obj, int):
            return str(obj, encoding='utf-8')
        elif isinstance(obj, float):
            return str(obj, encoding='utf-8')
        else:
            return super(json.NpEncoder, self).default(obj)