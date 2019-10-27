from google.cloud import language_v1
from google.cloud.language_v1 import enums
import numpy as np
import matplotlib.pyplot as plt

def sample_analyze_sentiment(text_content):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'I am so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_sentiment(document, encoding_type=encoding_type)
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )
    # Get sentiment for all sentences in the document
    return response.sentences


#get text doc

###text####
txtFile = open('13chil.txt','r')
text = txtFile.read()
sentiment_responses = sample_analyze_sentiment(text)
txtFile.close()

txtFile = open('13chil.txt', 'r')
badWordList = []
wordDic = {}
#if word in badword list, add to dictionary <word:count>
for line in txtFile.readlines():
    words = [word.strip() for word in line]
    for word in words:
        if word in badWordList:
            if word in wordDic:
                wordDic[word] += 1
            else:
                wordDic[word] = 1
wordsX = wordDic.keys()
countY = wordDic.values()
plt.bar(wordsX, countY)
plt.title('Bad Words')
plt.xlabel('Negative Word')
plt.ylabel('Count')

x = []
y = []
for sentence in sentiment_responses:
    x.append(sentence.sentiment.score)
    y.append(sentence.sentiment.magnitude)

plt.scatter(x, y)
plt.title('Scatter plot pythonspot.com')
plt.xlabel('x')
plt.ylabel('y')
plt.show()