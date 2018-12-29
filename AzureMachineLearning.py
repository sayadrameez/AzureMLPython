import requests 
import nltk
import pandas as pd
from nltk.probability import FreqDist
response = requests.get('https://raw.githubusercontent.com/sayadrameez/Azure-Learning/master/Moon.txt')
#doc1= open(response.files(),"r")
#doc1txt = doc1.read()
print(response.text)
from string import punctuation
txt = ''.join(c for c in response.text if not c.isdigit())
txt = ''.join(c for c in txt if c not in punctuation).lower()
print(txt)
words = nltk.tokenize.word_tokenize(txt)
fdist = FreqDist(words)
count_frame = pd.DataFrame(fdist,index =[0]).T
count_frame.columns = ['Count']
print(count_frame)

###%matplotlib inline
#import matplotlib.pyplot as plt
#counts = count_frame.sort_values('Count',ascending =False)
#fig = plt.figure(figsize=(16,9))
#ax = fig.gca()
#counts['Count'][:60].plot(kind='bar',ax=ax)
#ax.set_title('Frequency of the most common words')
#ax.set_ylabel('Frequency of word')
#ax.set_xlabel('Word')
##plt.show()
from nltk.corpus import stopwords

txt = ' '.join([word for word in txt.split() if word not in (stopwords.words('english'))])
print(txt)
words = nltk.tokenize.word_tokenize(txt)
fdist = FreqDist(words)
count_frame = pd.DataFrame(fdist,index =[0]).T
count_frame.columns = ['Count']
counts = count_frame.sort_values('Count',ascending = False)
#fig = plt.figure(figsize=(16,9))
#ax = fig.gca()
#counts['Count'][:60].plot(kind='bar',ax=ax)
#ax.set_title('Frequency of the most common words')
#ax.set_ylabel('Frequency of the word')
#ax.set_xlabel('Word')
#plt.show()
response = requests.get('https://raw.githubusercontent.com/sayadrameez/AI-Introduction/master/files/Gettysburg.txt')

txt2 = ''.join(c for c in response.text if not c.isdigit())
txt2 = ''.join(c for c in txt2 if c not in punctuation).lower()
txt2 = ' '.join([word for word in txt2.split() if word not in (stopwords.words('english'))])
print(txt2)
response = requests.get('https://raw.githubusercontent.com/sayadrameez/AI-Introduction/master/files/Cognitive.txt')

txt3 = ''.join(c for c in response.text if not c.isdigit())
txt3 = ''.join(c for c in txt3 if c not in punctuation).lower()
txt3 = ' '.join([word for word in txt3.split() if word not in (stopwords.words('english'))])
print(txt3)

import math
from textblob import TextBlob as tb
def tf(word,doc):
    return doc.words.count(word) / len(doc.words)

def contains(word,docs):
    return sum(1 for doc in docs if word in doc.words)

def idf(word,docs):
    return math.log(len(docs) / (1 + contains(word,docs)))

def tfidf(word,doc,docs):
    return tf(word,doc) * idf(word,docs)

doc1 = tb(txt)
doc2 = tb(txt2)
doc3 = tb(txt3)

docs = [doc1,doc2,doc3]

for i,doc in enumerate(docs):
    print('Top documents in {}'.format(i + 1))
    scores = {word:tfidf(word,doc,docs) for word in doc.words}
    sorted_words = sorted(scores.items(),key=lambda x:x[1],reverse=True)
    for word,score in sorted_words[:3]:
            print('\t Word:{} , TF IDF:{} '.format(word,round(score,5)))