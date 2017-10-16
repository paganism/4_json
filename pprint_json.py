import json


def load_data(filepath):
    with open(filepath, 'r') as f:
        return json.loads(f.read())    


def pretty_print_json(jsondata):
    return json.dumps(jsondata, indent=4, sort_keys=True)


if __name__ == '__main__':
    action = pretty_print_json(load_data('rawjson.txt'))
    print(action)
