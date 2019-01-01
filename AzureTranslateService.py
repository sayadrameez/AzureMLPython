transTextKey = "526e7343a4334bb4982e966f8f375baf"

import requests
import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
import json
import urllib
from xml.etree import ElementTree


textToTranslate = input('Please enter some text: \n')
fromLangCode = input('What language is this?: \n') 
toLangCode = input('To what language would you like it translated?: \n') 

try:
    # Connect to server to get the Access Token
    apiKey = transTextKey
    params = ""
    headers = {"Ocp-Apim-Subscription-Key": apiKey}
    AccessTokenHost = "api.cognitive.microsoft.com"
    path = "/sts/v1.0/issueToken"

    conn = http.client.HTTPSConnection(AccessTokenHost)
    conn.request("POST", path, params, headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    accesstoken = "Bearer " + data.decode("UTF-8")


    # Define the request headers.
    headers = {
        'Authorization': accesstoken
    }

    # Define the parameters
    params = urllib.parse.urlencode({
        "text": textToTranslate,
        "to": toLangCode,
        "from": fromLangCode
    })

    # Execute the REST API call and get the response.
    conn = http.client.HTTPSConnection("api.microsofttranslator.com")
    conn.request("GET", "/V2/Http.svc/Translate?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    translation = ElementTree.fromstring(data.decode("utf-8"))
    print(translation.text)

    conn.close()
    
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
