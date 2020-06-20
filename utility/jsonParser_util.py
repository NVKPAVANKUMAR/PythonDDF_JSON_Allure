import json


def parse_json(name, node, key):
    with open("./data/data.json", "r") as read_file:
        data = json.load(read_file)
        return data[name][node][key]


def json_length(name):
    with open("./data/data.json", "r") as read_file:
        data = json.load(read_file)
        return len(data[name])


def write_json(name, node, key, value):
    with open("./data/data.json", 'r') as f:
        data = json.loads(f.read())
    data[name][node][key] = value
    with open("./data/data.json", 'w') as f:
        f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')))


