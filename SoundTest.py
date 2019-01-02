import IPython

import requests
r = requests.get('https://raw.githubusercontent.com/MicrosoftLearning/AI-Introduction/master/files/RainSpain.wav')

IPython.display.Audio(r.content, autoplay=True)

#Works
from pydub import AudioSegment
from pydub.playback import play
import io 
from io import BytesIO
song = AudioSegment.from_file(BytesIO(r.content), format="wav")
play(song)