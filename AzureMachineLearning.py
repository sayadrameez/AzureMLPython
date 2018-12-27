import requests 
response = requests.get('https://raw.githubusercontent.com/sayadrameez/Azure-Learning/master/Moon.txt')
#doc1= open(response.files(),"r")
#doc1txt = doc1.read()
print(response.text)
from string import punctuation
txt = ''.join(c for c in response.text if not c.isdigit())
txt= ''.join(c for c in txt if c not in punctuation).lower()
print(txt)