import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

#nltk.download(vader_lexicon)

analyzer = SentimentIntensityAnalyzer()

text1 = 'Hey, what a beautiful day! How amazing it is!'
analyze = analyzer.polarity_scores(text1) # get coef
print(analyze)
print(type(analyze))

# access compound key of dict
compound = analyze['compound']
print(compound)

if compound > 0:
    print('Positive')
else:
    print('Negative')