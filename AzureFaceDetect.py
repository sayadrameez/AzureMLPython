import json
from matplotlib import pyplot
from PIL import Image
from io import BytesIO
from PIL import ImageDraw
import requests
faceUri = 'https://centralus.api.cognitive.microsoft.com/face/v1.0'
faceKey = 'e7aea26f8f204eb3bcfc28be066a4e32'
########### Python 3.2 #############
import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
img_url = 'https://github.com/sayadrameez/AI-Introduction/raw/master/files/graeme1.jpg'
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': faceKey
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    #'returnFaceAttributes': 'age'
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
})

#body =
#"{'url':'https://github.com/sayadrameez/AI-Introduction/raw/master/files/graeme1.jpg'}"
try:
    def get_facedata(body):
        conn = http.client.HTTPSConnection('centralus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        parsedData = json.loads(data)
        face1 = parsedData[0]['faceId']
        print('face1:' + face1)
        conn.close()
        return parsedData
    face1 = get_facedata("{'url':'https://github.com/sayadrameez/AI-Introduction/raw/master/files/graeme1.jpg'}")
    response = requests.get('https://github.com/sayadrameez/AI-Introduction/raw/master/files/graeme1.jpg')    
    img = Image.open(BytesIO(response.content))
    color = 'blue'

    

    def drawLineOverFace(face1Img,color,img):
        if face1Img is not None:
            draw = ImageDraw.Draw(img)
            for currFace in face1Img:
                faceRectangle = currFace['faceRectangle']
                left = faceRectangle['left']
                top = faceRectangle['top']
                width = faceRectangle['width']
                height = faceRectangle['height']
                draw.line([(left,top),(left + width,top)],fill=color,width=5)
                draw.line([(left + width,top),(left + width,top + height)],fill=color,width=5)
                draw.line([(left + width,top + height),(left ,top + height)],fill=color,width=5)
                draw.line([(left ,top + height),(left ,top)],fill=color,width=5)
        pyplot.imshow(img)
        pyplot.show()

    drawLineOverFace(face1,color,img)
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

face2 = get_facedata("{'url':'https://github.com/sayadrameez/AI-Introduction/raw/master/files/graeme2.jpg'}")
####################################
params = urllib.parse.urlencode({
})

body = {
    'faceId1':face1[0]['faceId'],
    'faceId2':face2[0]['faceId']
    }

try:
    conn = http.client.HTTPSConnection('centralus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/verify?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
    parsedData = json.loads(data)

    response = requests.get('https://github.com/sayadrameez/AI-Introduction/raw/master/files/graeme2.jpg')    
    img = Image.open(BytesIO(response.content))
    color = 'lightgreen' if parsedData['isIdentical'] == True else 'red'

    drawLineOverFace(face2,color,img)

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
face3 = get_facedata("{'url':'https://github.com/sayadrameez/AI-Introduction/raw/master/files/graeme3.jpg'}")

body = {
    'faceId1':face1[0]['faceId'],
    'faceId2':face3[0]['faceId']
    }

try:
    conn = http.client.HTTPSConnection('centralus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/verify?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
    parsedData = json.loads(data)

    response = requests.get('https://github.com/sayadrameez/AI-Introduction/raw/master/files/graeme3.jpg')    
    img = Image.open(BytesIO(response.content))
    color = 'lightgreen' if parsedData['isIdentical'] == True else 'red'

    drawLineOverFace(face3,color,img)

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))