#%%
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

########### Python 3.2 ############# List Videos
import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64

headers = {
}

params = urllib.parse.urlencode({
    # Request parameters
    'pageSize': '{integer}',
    'skip': '{integer}',
})

try:
    conn = http.client.HTTPSConnection('api.videoindexer.ai')
    #conn.request("GET",
    #"/{location}/Accounts/{accountId}/Videos?accessToken={accessToken}&%s" %
    #params, "{body}", headers)
    conn.request("GET", "/%s/Accounts/%s/Videos?accessToken=%s&%s" % (viLocation,viaccountid,accessToken ,params), "{body}", headers)

    response = conn.getresponse()
    data = response.read()
    print(data)
    parsedData = json.loads(data.decode('UTF-8'))
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
for result in parsedData['results']:
    if result['name'] == 'FileName':
        videoid = result['id']                      


########### Python 3.2 #############
import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64

headers = {
}

params = urllib.parse.urlencode({
    # Request parameters
    'accessToken': accessToken,
    'language': 'English',
})

try:
    conn = http.client.HTTPSConnection('api.videoindexer.ai')
    #conn.request("GET",
    #"/{location}/Accounts/{accountId}/Videos/{videoId}/Index?%s" % params,
    #"{body}", headers)
    conn.request("GET", "/%s/Accounts/%s/Videos/%s/Index?%s" % (viLocation,viaccountid,videoid, params), "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    parsedData = json.loads(data.decode('UTF-8'))

    print(json.dumps(parsedData,sort_keys=True,indent=2))
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

print('State of the video is %s' % parsedData['state'])


########### Python 3.2 ############# Get Video Level Access Token
import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': visubscriptionkey,
}

params = urllib.parse.urlencode({
    # Request parameters
    'allowEdit': True,
})

try:
    conn = http.client.HTTPSConnection('api.videoindexer.ai')
    #conn.request("GET",
    #"/auth/{location}/Accounts/{accountId}/Videos/{videoId}/AccessToken?%s" %
    #params, "{body}", headers)
    conn.request("GET", "/auth/%s/Accounts/%s/Videos/%s/AccessToken?%s" % (viLocation,viaccountid,videoid,params), "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)

    videoaccesstoken = data.decode('UTF-8').replace('"','')
    print(videoaccesstoken)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


from IPython.core.display import HTML

playerUrl = 'https://videoindexer.ai/embed/player/{0}/{1}/?accessToken={2}'.format(viaccountid,videoid,videoaccesstoken)
print(playerUrl)
#%%
print(playerUrl)
iframeHtml = str('<iframe width="900" height="600" src="' + playerUrl + '"')
print(iframeHtml)
#HTML('<iframe width=900 height=600 src="%s"' % playerUrl)
thumbnailid = parsedData['summarizedInsights']['thumbnailId']
########### Python 3.2 ############# --- Thumbnail
import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64

headers = {
}

params = urllib.parse.urlencode({
    # Request parameters
    'accessToken': videoaccesstoken,
    #'format': '{string}',
})
from PIL import Image
from io import BytesIO
from matplotlib import pyplot 
try:
    conn = http.client.HTTPSConnection('api.videoindexer.ai')
    #conn.request("GET",
    #"/{location}/Accounts/{accountId}/Videos/{videoId}/Thumbnails/{thumbnailId}?%s"
    #% params, "{body}", headers)
    conn.request("GET", "/%s/Accounts/%s/Videos/%s/Thumbnails/%s?%s" % (viLocation,viaccountid,videoid,thumbnailid, params), "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    #%%
    img = Image.open(BytesIO(data))
    pyplot.imshow(img)
    pyplot.show()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
