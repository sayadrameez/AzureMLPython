import requests
from string import punctuation
import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import pandas as pd
import matplotlib.pyplot as plt

from nltk.stem.porter import PorterStemmer
response = requests.get('https://raw.githubusercontent.com/sayadrameez/AI-Introduction/master/files/KennedyInaugural.txt')
txt3 = ''.join(c for c in response.text if not c.isdigit())
txt3 = ''.join(c for c in txt3 if c not in punctuation).lower()
txt3 = ' '.join([word for word in txt3.split() if word not in (stopwords.words('english'))])
print(txt3)
words = nltk.tokenize.word_tokenize(txt3)
fdist = FreqDist(words)

count_frame = pd.DataFrame(fdist,index =[0]).T
count_frame.columns = ['Count']
counts = count_frame.sort_values('Count',ascending = False)
fig = plt.figure(figsize=(16,9))
ax = fig.gca()
counts['Count'][:60].plot(kind='bar',ax=ax)
ax.set_title('Frequency of the most common words')
ax.set_ylabel('Frequency of the word')
ax.set_xlabel('Word')
plt.show()
ps = PorterStemmer()
stems = [ps.stem(word) for word in words]
fdist = FreqDist(stems)

count_frame = pd.DataFrame(fdist,index =[0]).T
count_frame.columns = ['Count']
counts = count_frame.sort_values('Count',ascending = False)
fig = plt.figure(figsize=(16,9))
ax = fig.gca()
counts['Count'][:60].plot(kind='bar',ax=ax)
ax.set_title('Stemmed Frequency of the most common words')
ax.set_ylabel('Frequency of the word')
ax.set_xlabel('Word')
plt.show()