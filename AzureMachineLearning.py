import requests 
response = requests.get('https://raw.githubusercontent.com/sayadrameez/Azure-Learning/master/Moon.txt')
#doc1= open(response.files(),"r")
#doc1txt = doc1.read()
print(response.text)