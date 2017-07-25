#!/usr/bin/python3

import json
import sys
import urllib.request

# NLNOG Ring Active Ring Nodes:

with urllib.request.urlopen("https://ring.nlnog.net/api/1.0/nodes/active") as url:
    data = json.loads(url.read().decode())

activenodes = {}

for item in data['results']['nodes']:
    activenodes[item['hostname']] = (item['hostname'].split('.', 1)[0] + " - AS" + str(item['asn']) + " - " + item['countrycode'])

# Print Title:

print("+ NLNOG-Ring")
print("menu = NLNOG Ring")
print("title = NLNOG Ring")

# Nodes:

for key in sorted(activenodes):
    print("")
    print("++ %s" % (key.split('.', 1)[0]))
    print("menu = %s" % (key.split('.', 1)[0]))
    print("title = %s" % (activenodes[key]))
    print("probe = FPing")
    print("host = %s" % (key))
    print("alerts = highloss,majorloss")
