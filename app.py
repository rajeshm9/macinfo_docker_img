import sys
import urllib.request
import json



if len (sys.argv) != 3 :
#    print ("Usage: python "+sys.argv[0]+" MAC_ADDRESS")
    print ("Usage: docker run -e API_KEY=<api_key> <imagename> <mac_address>")
    sys.exit (1)
    
mac=sys.argv[1]
api_key=sys.argv[2]

try:
    contents = urllib.request.urlopen(urllib.request.Request(
        "https://api.macaddress.io/v1?output=json&search="+mac,
        headers={"X-Authentication-Token" : api_key }
    )).read()
    resp = json.loads(contents)
    print ("MAC_ADDRESS="+mac+",COMPANY_NAME="+resp['vendorDetails']['companyName'])
    
except urllib.error.URLError as e:
    print("We have error for MAC=["+mac+"] !! " + e.reason+ " Http Code="+str(e.code))
    
    
