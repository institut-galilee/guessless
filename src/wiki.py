import requests
import json

def word(word) :
	response = requests.get("https://en.wikipedia.org/w/api.php?format=json&action=opensearch&search=" + word)
	suggestions = json.loads(response.content)
	try:
		return suggestions[1][0]
	except IndexError:
		return suggestions[0]

def search(name) :
    response = requests.get("https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=0&titles=" + name)
    if (response.status_code == 200):
        data = json.loads(response.content.decode('utf-8'))
        for key in data['query']['pages']:
            if (key != '-1'):
                return data['query']['pages'][key]['extract']
