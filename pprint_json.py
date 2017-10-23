import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as f:
        raw_data = f.read()
    return raw_data


def pretty_print_json(data_for_pprint):
    prettyjson = json.dumps(json.loads(data_for_pprint), indent=4, sort_keys=True, ensure_ascii=False)
    return prettyjson


if __name__ == '__main__':
    filepath = sys.argv[1]
    pretty_print_json(load_data(filepath))
