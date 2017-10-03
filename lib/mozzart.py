import requests
import json

url = 'https://www.mozzartbet.com/MozzartWS/oddsLive/offer'

post_variables = {
    "sports":
        [1,5,2,55,7,54,6,9,8,4,58,56,3,19,14,15,10,27,28,30,31,59,60,61,62,63,64,12,48,50,65,77],
    "dateRange":
        {
            "from": None,
            "to": None
        },
    "matchStatus": ["READY"],
    "matchSorting": "BY_TIME",
    "selectedCompetitions": [],
    "selectedGames": None,
    "languageId": 1,
    "matchNumber": None,
    "favouriteMatchNumbers": [],
    "pageNumber": 1
}

if __name__ == '__main__':
    response = requests.post(url=url, json=post_variables, verify=False)
    resp_data = json.dumps(response.json())
    file = open('json.json', 'w')
    file.write(resp_data)
    file.close()
