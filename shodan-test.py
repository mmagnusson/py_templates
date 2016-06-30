#!/usr/bin/python

# examples are using Py2, but read a tweet that said Py3 works?  it's REST, so requests should work?

# API docs https://developer.shodan.io/api

# base URL for API use https://api.shodan.io
# /shodan/host/{ip}
# /shodan/host/count
# /shodan/host/search
# /shodan/host/search/tokens
# /shodan/ports
# /shodan/protocols
# /shodan/scan/{id}
# /shodan/services
# /shodan/query
# /shodan/query/search
# /shodan/query/tags
# POST
# /shodan/scan
# /shodan/scan/internet

# 

import shodan

SHODAN_API_KEY = ''

api = shodan.Shodan(SHODAN_API_KEY)

# Wrap the request in a try/ except block to catch errors
try:
        # Search Shodan
        search = ("apache")
        results = api.search(search)

        # Show the results
        print('Results found: %s' % results['total'])
        for result in results['matches']:
                print('IP: %s' % result['ip_str'])
                print(result['data'])
                print('')
except shodan.APIError as e:
        print('Error: %s' % e)
