#!/usr/bin/python
# -*- coding: Cp1251 -*-

'''
Created on 26 апр. 2016 г.

@author: ggolyshev
'''
import urllib.request
import urllib.parse

import json

if __name__ == '__main__':
    # serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
    serviceurl = 'http://python-data.dr-chuck.net/geojson?'

    while True:
        address = input('Enter location: ')
        if len(address) < 1 : break

        url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
        print ('Retrieving', url)
        uh = urllib.request.urlopen(url)
        data = uh.read()
        print ('Retrieved',len(data),'characters')
        
        try: js = json.loads(data.decode('utf-8'))
        except: js = None
        if 'status' not in js or js['status'] != 'OK':
           print ('==== Failure To Retrieve ====')
           print (data)
           continue
        
        print(js["results"][0]["place_id"])
