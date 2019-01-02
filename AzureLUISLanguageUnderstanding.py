from matplotlib import pyplot
from PIL import Image
import requests
from io import BytesIO
import json

endpointurl = 'https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/5eb952f8-d9ff-441d-8677-f1f655141569?verbose=true&timezoneOffset=-360&subscription-key=4494bf90e13d4795a070d7ecbe81d4c6&q='

command = input('Please enter a command: \n')

endpoint = endpointurl + command.replace(" ","+")
response = requests.get(endpoint)
data = json.loads(response.content.decode("UTF-8"))
intent = data["topScoringIntent"]["intent"]
if(intent == "Light On"):
    img_url = 'https://github.com/sayadrameez/AI-Introduction/raw/master/files/LightOn.jpg'
elif(intent == "Light Off"):
    img_url = 'https://github.com/sayadrameez/AI-Introduction/raw/master/files/LightOff.jpg'
else:
    img_url = 'https://github.com/sayadrameez/AI-Introduction/raw/master/files/Dunno.jpg'
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))
pyplot.imshow(img)
pyplot.show()