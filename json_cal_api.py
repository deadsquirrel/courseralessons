import urllib
import json

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
#serviceurl = 'http://python-data.dr-chuck.net/geojson?'
## read this!!
## https://developers.google.com/google-apps/calendar/quickstart/python#step_2_install_the_google_client_library


while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
#        print data
        continue

    print json.dumps(js, indent=4)
    pl_id = js["results"][0]["place_id"]
    print pl_id