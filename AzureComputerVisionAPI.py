visionURL = 'eastus.api.cognitive.microsoft.com'
visionKey = '39c8a9ec7e1643b79bc4de572699bac4'

from matplotlib import pyplot
from PIL import Image
import requests
from io import BytesIO

img_url = 'https://github.com/sayadrameez/AI-Introduction/raw/master/files/graeme2.jpg'

def get_features(img_url):
    import http.client
    import urllib.request
    import urllib.parse
    import urllib.error
    import base64
    import json

    headers = {
        'Content-Type':'application/json',
        'Ocp-Apim-Subscription-Key':visionKey
        }
    params = urllib.parse.urlencode({
        'visualFeatures':'Categories,Description,Color',
        'language':'en'
        })

    body = "{'url':'" + img_url + "'}"

    try:
        conn = http.client.HTTPSConnection(visionURL)
        conn.request("POST","/vision/v1.0/analyze?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        parsed = json.loads(data)
        
        conn.close()
        desc = parsed['description']['captions'][0]['text']
        print(desc)
        response = requests.get(img_url)
        img = Image.open(BytesIO(response.content))
        pyplot.imshow(img)
        pyplot.show()
        if response is not None:
            return parsed
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

json_data = get_features(img_url)

img_url = 'https://github.com/sayadrameez/AI-Introduction/raw/master/files/uke.jpg'
json_data = get_features(img_url)

img_url ='https://github.com/sayadrameez/AI-Introduction/raw/master/files/soccer.jpg'
json_data = get_features(img_url)