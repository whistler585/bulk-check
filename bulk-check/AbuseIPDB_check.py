import requests
import json

#######################################################

# usage: python AbuseIPDB_check.py > <path to output file>

# Go here for more information regarding AbuseIPDB: https://www.abuseipdb.com/

#######################################################

#Opens a seed file and interates through each line.  Use ranges or CIDR in the seed file if you're using the "check-block" call. 
#Use only IP addresses in the seed file if you're scanning single addresses. 

file1 = open('<path to cidr file>', 'r')
count = 0

for line in file1:
    count += 1
    
        
###########Check-Block################ 

####Uncomment if you're checking CIDR or ranges - comment if you're not####          
    url = 'https://api.abuseipdb.com/api/v2/check-block'
    querystring = {
    	'network': line.strip(),
    	'maxAgeInDays':'365',
	}
    headers = {
         'Accept': 'application/json',
         'Key': '<abuseipdb api key - ask Pat>'
         }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

		# Formatted output
    decodedResponse = json.loads(response.text)
    print json.dumps(decodedResponse, sort_keys=True, indent=4)

file1.close()

###########Check IP Address#############

####Uncomment if you're checking IP addresses - comment if you're not####

#    url = 'https://api.abuseipdb.com/api/v2/check'
#    querystring = {
#    	'network': line.strip(),
#    	'maxAgeInDays':'365',
#	}
#    headers = {
#         'Accept': 'application/json',
#         'Key': '<abuseipdb api key - ask Pat>'
#         }
#
#    response = requests.request(method='GET', url=url, headers=headers, params=querystring)
#
#		# Formatted output
#    decodedResponse = json.loads(response.text)
#    print json.dumps(decodedResponse, sort_keys=True, indent=4)

#file1.close()