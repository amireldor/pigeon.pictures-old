import settings
import urllib.request
from random import choice


def makeRequestUrl(settings):
    nouns = ("pigeon", "dove", "pigeonhole")
    adjectives = ("", "nice", "pretty", "lovely", "elegant", "real", "flying", "eating")
    pigeon_query = "{}%20{}".format(choice(adjectives), choice(nouns))

    return "https://www.googleapis.com/customsearch/v1" \
           "?q={}&cx={}&imgType=photo" \
           "&safe=medium&searchType=image&fields=items%2Flink&key={}" \
           .format(pigeon_query, settings.CSE_ID, settings.API_KEY)

request_url = makeRequestUrl(settings)
print(request_url)

response = urllib.request.urlopen(request_url)
raw = response.read()
data = raw.decode("latin-1")
response.close()

with open("pigeons.json", "w") as json_file:
    json_file.write(data)

