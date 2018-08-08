import requests
import json
def geocode(address):
    paramaters={'address':address,'sensor':'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    resp = requests.get(base,params=paramaters)
    j = resp.json()
    print(j['results'][0]['geometry']['location'])

if __name__=='__main__':
    geocode('207 N.Definace St,Archbold,OH')