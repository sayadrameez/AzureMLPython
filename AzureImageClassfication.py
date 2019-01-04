from matplotlib import pyplot
from PIL import Image
import requests
from io import BytesIO
import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
import json

img_url = 'https://github.com/sayadrameez/AI-Introduction/raw/master/files/Vision/Test.jpg'


'1fe8cc76-7ace-4829-92e7-f25940e8f011'

headers = {
    'Content-Type':'application/json',
    'Prediction-key':'ab451f53c2064fb49276eb96a492067b'
    }

params = urllib.parse.urlencode({
    })
body = "{'Url':'" + img_url + "'}"

try:
    conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
    conn.request("POST",'/customvision/v2.0/Prediction/1fe8cc76-7ace-4829-92e7-f25940e8f011/url',body,headers)
    response = conn.getresponse()
    data = response.read()
    parsed = json.loads(data)

    sorted_predictions = dict(parsed)
    sorted_predictions['predictions'] = sorted(parsed['predictions'],key= lambda x: x['probability'])
    print(sorted_predictions['predictions'][0]['tagName'])
    conn.close()

    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content))
    pyplot.imshow(img)
    pyplot.show()

except Exception as e:
    print(e.errno)
    print(e.strerror)

