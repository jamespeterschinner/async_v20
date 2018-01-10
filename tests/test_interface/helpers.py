import ujson as json
def sort_json(x):
    return json.dumps(json.loads(x), sort_keys=True)

def order_dict(obj):
    if isinstance(obj, dict):
        return sorted((k, order_dict(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(order_dict(x) for x in obj)
    else:
        return obj
