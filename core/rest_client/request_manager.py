import requests
import yaml

global config_data
config_data = yaml.load(open('environment.yml'))


# Class that performs API requests.
class RequestManager:

    def __init__(self):
        self.method = ''
        self.endpoint = ''
        self.headers = {}
        self.body = {}
        self.parameters = {}
        self.base_url = config_data['api_url']
        self.authentication = (config_data['user'], config_data['pass'])

    def set_headers(self, headers):
        self.headers = headers

    def set_parameters(self, parameters):
        self.parameters = parameters

    def set_body(self, body):
        self.body = body

    def set_base_url(self, base_url):
        self.base_url = base_url

    def set_method(self, method):
        self.method = method

    def set_endpoint(self, endpoint):
        self.endpoint = endpoint

    def get_body(self):
        return self.body

    def get_headers(self):
        return self.headers

    def get_parameters(self):
        return self.parameters

    def get_base_url(self):
        return self.base_url

    def get_method(self):
        return self.method

    def get_endpoint(self):
        return self.endpoint

    def build_url(self):
        return "{}{}".format(self.base_url, self.endpoint)

    def execute_request(self):
        """
        Performs an API request.
        """
        uri = self.build_url()
        if self.method == 'GET':
            return requests.get(uri, headers=self.headers, auth=self.authentication)
        elif self.method == 'POST':
            return requests.post(uri, headers=self.headers, auth=self.authentication, data=self.get_body())
