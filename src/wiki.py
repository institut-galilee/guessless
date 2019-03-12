import requests
import json

def word(word) :
	response = requests.get("https://fr.wikipedia.org/w/api.php?format=json&action=opensearch&search=" + word)
	suggestions = json.loads(response.content)
	return suggestions[1][0]

def search(name) :
    response = requests.get("https://fr.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=" + word(translate(name)))
    if (response.status_code == 200):
        data = json.loads(response.content)
        for key in data['query']['pages']:
            if (key != '-1'):
                print(data['query']['pages'][key]['extract'])

def translate(word) :
	return word

search("smartphone")
