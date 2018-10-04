import httplib, urllib, base64
headers = {
    # Request headers
    'api_key': '£££',
}
latitude = ['25.365351']
longitude = ['49.578335'] 
i=0
j=0
for i in range(0,len(latitude)):
        params = urllib.urlencode({
            # Request parameters
            'lat': latitude[i],
            'long': longitude[j],
            'language': 'A',
            'format': 'json',
            'encode': '{string}',
        })

        try:
            conn = httplib.HTTPSConnection('apina.address.gov.sa')
            conn.request("GET", "/NationalAddress/v3.1/Address/address-geocode?%s" % params, "{body}", headers)
            response = conn.getresponse()
            data = response.read()

            file=open('amir.txt','w')
            file.write(data)
            print(data)
            conn.close()
        except Exception as e:
            print("erorr has occured")