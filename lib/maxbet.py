import requests
import json

url = 'https://www.maxbet.rs/ibet/async/live/multi/basic/1658176973.json'  # FAIL


if __name__ == '__main__':
    response = requests.post(url=url, verify=False)
    resp_data = json.dumps(response.json())
    file = open('json.json', 'w')
    file.write(resp_data)
    file.close()
