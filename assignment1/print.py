import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=coursera")
print json.load(response)
