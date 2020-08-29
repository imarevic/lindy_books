import yaml
import requests
import src.consts as c

# helper functions
def get_api_key(filename):

    with open(filename) as f:
        data = yaml.safe_load(f)
    return data[c.api_key_name]

def get_data(offset, api_token):

    url = c.base_url + '?offset=' + str(offset) + '&' + 'api-key=' + api_token
    return requests.get(url).json()
