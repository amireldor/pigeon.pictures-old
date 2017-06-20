import settings
import urllib.request


def makeRequestUrl(settings):
    return "http://www.google.com"

request_url = makeRequestUrl(settings)

response = urllib.request.urlopen(request_url)
raw = response.read()
data = raw.decode("latin-1")
response.close()

with open("pigeons.json", "w") as json_file:
    json_file.write(data)

