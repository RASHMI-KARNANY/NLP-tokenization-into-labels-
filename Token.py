import nltk
import matplotlib.pyplot as plt
import random

test='There are a lot of butterflies flushing in my stomach #butterflyday!!!!! '
print(test)

nltk.download('stopwords')
import re                                  # library for regular expression operations
import string                              # for string operations

from nltk.corpus import stopwords          # module for stop words that come with NLTK
from nltk.stem import PorterStemmer        # module for stemming
from nltk.tokenize import TweetTokenizer  

test2=re.sub(r'^RT[\s]+','',test)
test3=re.sub(r'https?:\/\/.*[\r\n]*','',test2)
test=re.sub(r'#','',test3)
print(test)

token=TweetTokenizer(preserve_case=False,reduce_len=True,strip_handles=True)
tt=token.tokenize(test)
print(tt)
stopword=stopwords.words('english')
final=[]
for word in tt:
  if(word not in stopword and word not in string.punctuation):
    final.append(word)

print(final)

stemmer=PorterStemmer()
final2=[]
for word in final:
    stem_word=stemmer.stem(word)
    final2.append(stem_word)

print(final2)
