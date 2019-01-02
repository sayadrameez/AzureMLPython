import speech_recognition as sr
from matplotlib.pyplot import imshow
from PIL import Image
import requests
from io import BytesIO
import json 
# Set up API configuration
endpointUrl = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/5eb952f8-d9ff-441d-8677-f1f655141569?verbose=true&timezoneOffset=-360&subscription-key=4494bf90e13d4795a070d7ecbe81d4c6&q="

resp = requests.get('https://github.com/sayadrameez/AI-Introduction/raw/master/files/LightOn.wav')

#Works
from pydub import AudioSegment
from pydub.playback import play
import io 
from io import BytesIO
song = AudioSegment.from_file(BytesIO(resp.content), format="wav")


speechKey = '2a6c8e2de7724dbe94a0ebfdea59a803'
# Specify which audio file to use
#audioFile = "LightOn.wav"

#audio = BytesIO(resp.content)
# Convert Audio to Audio Source Format
audio = sr.AudioData(resp.content, 16000, 2)

# Read the audio file
r = sr.Recognizer()
#with sr.AudioFile(audioFile) as source:
#    audio = r.record(source)
#r = sr.Recognizer()
with sr.Microphone() as source: 
    play(song)
    audio = r.listen(source)
try:
    # transcribe speech using the Bing Speech API
    transcription = r.recognize_bing(audio, key=speechKey)
    
    # Call the LUIS service and get the JSON response
    endpoint = endpointUrl + transcription.replace(" ","+")
    response = requests.get(endpoint)
    data = json.loads(response.content.decode("UTF-8"))

    # Identify the top scoring intent
    intent = data["topScoringIntent"]["intent"]
    if (intent == "Light On"):
        img_url = 'https://raw.githubusercontent.com/MicrosoftLearning/AI-Introduction/master/files/LightOn.jpg'
    elif (intent == "Light Off"):
        img_url = 'https://raw.githubusercontent.com/MicrosoftLearning/AI-Introduction/master/files/LightOff.jpg'
    else:
        img_url = 'https://raw.githubusercontent.com/MicrosoftLearning/AI-Introduction/master/files/Dunno.jpg'

    # Get the appropriate image and show it
    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content))
    imshow(img)
    
except sr.UnknownValueError:
    print("Bing Speech could not understand audio")
except sr.RequestError as e:
    print (e)
    print("Could not request results from the Bing Speech service; {0}".format(e))
