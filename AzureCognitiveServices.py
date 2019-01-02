textAnalyticsUri = 'centralus.api.cognitive.microsoft.com'
textKey = '2f981c2fa84b4d03aa5437cdbf094337'

import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
import json
import urllib
import requests


headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': textKey,
    'Accept':'application/json'
}

params = urllib.parse.urlencode({
})

response = requests.get('https://raw.githubusercontent.com/sayadrameez/AI-Introduction/master/files/Gettysburg.txt')
doc1txt = response.text
response = requests.get('https://raw.githubusercontent.com/sayadrameez/AI-Introduction/master/files/Cognitive.txt')
doc2txt = response.text

body = {
  "documents": [{
      "language": "en",
      "id": "1",
      "text": doc1txt
    },
    {
      "language": "en",
      "id": "2",
      "text": doc2txt
    }]
}

try:
    conn = http.client.HTTPSConnection(textAnalyticsUri)
    conn.request("POST", "/text/analytics/v2.0/keyPhrases?%s" % params,str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    parsed = json.loads(data)
    for document in parsed['documents']:
        print('Document' + document["id"] + ' key phrases:')
        for phrase in document['keyPhrases']:
            print(' ' + phrase)
        print('----------------------------')
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


body = {
  "documents": [{
      "language": "en",
      "id": "1",
      "text": "I have when computers don't understand me!"
    },
    {
      "language": "en",
      "id": "2",
      "text": "Wow ! Azure cognitive services are the best!"
    }]
}

try:
    conn = http.client.HTTPSConnection(textAnalyticsUri)
    conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params,str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    parsed = json.loads(data)
    for document in parsed['documents']:
        sentiment = "negative" if document["score"] < 0.5 else "positive"
        print('Document :' + document['id'] + " = " + sentiment)
        print('----------------------------')
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

