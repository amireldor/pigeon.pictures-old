import settings
import urllib.request
from random import randint


def makeRequestUrl(settings):
    return "https://www.googleapis.com/customsearch/v1" \
           "?q=pigeon&cx={}&imgType=photo&dateRestrict=d{}" \
           "&safe=medium&searchType=image&fields=items%2Flink&key={}" \
           .format(settings.CSE_ID, randint(0, 100), settings.API_KEY)

request_url = makeRequestUrl(settings)

response = urllib.request.urlopen(request_url)
raw = response.read()
data = raw.decode("latin-1")
response.close()

with open("pigeons.json", "w") as json_file:
    json_file.write(data)

