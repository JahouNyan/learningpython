#import requests library
import requests
#do a request
url = input("Enter url request: ").strip()
r = requests.get(url)


#Check the status_code, if it is not 200, display an error and exit the program
if r.status_code is 200:
    print("ok")
        
else:
    print ("error")
    exit()

#Loop over the headers and display the key and value of every header.
for headers in r:
    headers = r.headers
for key in headers:
    value = headers[key]
    print(key, value)
#display the first 10 lines of text of the page the user provided
lines = r.text
lines= lines.split("\n")
for line in lines[:10]:
    print(line + " \n")
