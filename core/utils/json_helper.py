import json


class JsonHelper:

    @staticmethod
    def print_pretty_json(data):
        print(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')))
