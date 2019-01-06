import json
viLocation = 'trial'
viaccountid = 'c566388c-aab5-48f9-87fe-c2a688a68a15'
visubscriptionkey = '53346ad29e0a4e4d8a1e09e62fd11013'

########### Python 3.2 #############Access TOken
import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': visubscriptionkey
}

params = urllib.parse.urlencode({
    # Request parameters
    'allowEdit': True,
})

try:
    conn = http.client.HTTPSConnection('api.videoindexer.ai')
    #conn.request("GET", "/auth/{location}/Accounts/{accountId}/AccessToken?%s"
    #% params, "{body}", headers)
    conn.request("GET", "/auth/%s/Accounts/%s/AccessToken?%s" % (viLocation,viaccountid, params), "{body}", headers)

    response = conn.getresponse()
    data = response.read()
    print(data)
    accessToken = data.decode("UTF-8").replace('"','')
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


########### Python 3.2 #############
import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64

headers = {
    # Request headers
    'Content-Type': 'multipart/form-data',
}

video_url = 'https://github.com/sayadrameez/AI-Introduction/raw/master/files/vid.mp4'

params = urllib.parse.urlencode({
    # Request parameters
    #'description': '{string}',
    #'partition': '{string}',
    #'externalId': '{string}',
    #'callbackUrl': '{string}',
    #'metadata': '{string}',
    #'language': '{string}',
    'videoUrl': video_url,
    #'fileName': '{string}',
    #'indexingPreset': '{string}',
    #'streamingPreset': 'Default',
    #'linguisticModelId': '{string}',
    'privacy': 'Private',
    #'externalUrl': '{string}',
    #'assetId': '{string}',
    #'priority': '{string}',
    #'personModelId': '{string}',
    #'brandsCategories': '{string}',
})

try:
    conn = http.client.HTTPSConnection('api.videoindexer.ai')
    #conn.request("POST",
    #"/{location}/Accounts/{accountId}/Videos?accessToken={accessToken}&name={name}&%s"
    #% params, "{body}", headers)
    conn.request("POST", "/%s/Accounts/%s/Videos?accessToken=%s&name=%s&%s" % (viLocation,viaccountid, accessToken,'FileName', params), "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    parsed = json.loads(data.decode("UTF-8"))
    print(data)
    print(parsed)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


videoid = parsed['id']
print('vide od iud '.format(videoid))

