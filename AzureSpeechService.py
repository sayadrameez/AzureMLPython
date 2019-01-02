from IPython.display import Audio
import http.client
import urllib.parse
import json
from xml.etree import ElementTree
speechKey = '2a6c8e2de7724dbe94a0ebfdea59a803'
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print('Say something')
    audio = r.listen(source)
    try:
        transcription = r.recognize_bing(audio, key=speechKey)
        print('Here is what I heard')
        print('"' + transcription + '"')
    except sr.UnknownValueError:
        print('Audio was not clear')
    except sr.RequestError as e:
        print(e)
        print('Something went wrong {0}'.format(e))


myText = input('What would you like me to say ? : \n')

apiKey = speechKey
params = ""
headers = {"Ocp-Apim-Subscription-Key":apiKey}
AccessTokenHost = "westus.api.cognitive.microsoft.com"
path = "/sts/v1.0/issueToken"

conn = http.client.HTTPSConnection(AccessTokenHost)
conn.request("POST",path,params,headers)
response = conn.getresponse()
data = response.read()
conn.close()
accesstoken = data.decode("UTF-8")
print(accesstoken)

body = ElementTree.Element('speak', version='1.0')
body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
voice = ElementTree.SubElement(body, 'voice')
voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
voice.set('{http://www.w3.org/XML/1998/namespace}gender', 'Female')
voice.set('name', 'Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)')
voice.text = myText
headers = {"Content-type": "application/ssml+xml", 
           "X-Microsoft-OutputFormat": "riff-16khz-16bit-mono-pcm", 
           "Authorization": "Bearer " + accesstoken, 
           "X-Search-AppId": "07D3234E49CE426DAA29772419F436CA", 
           "X-Search-ClientID": "1ECFAE91408841A480F00935DC390960", 
           "User-Agent": "TTSForPython"}
bodytext =ElementTree.tostring(body)
print(bodytext)
#Connect to server to synthesize a wav from the text
conn = http.client.HTTPSConnection("westus.tts.speech.microsoft.com")
conn.request("POST", "/cognitiveservices/v1", bodytext, headers)
response = conn.getresponse()
data = response.read()
conn.close()

#Play the wav
Audio(data, autoplay=True)

from pydub import AudioSegment
from pydub.playback import play
import io 
from io import BytesIO
song = AudioSegment.from_file(BytesIO(data), format="wav")
play(song)