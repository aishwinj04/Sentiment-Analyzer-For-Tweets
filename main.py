import errno
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

x = nltk.corpus.twitter_samples.strings()[1]
print(x)

analyzer = SentimentIntensityAnalyzer()

text1 = 'Hey, what a beautiful day! How amazing it is!'
analyze = analyzer.polarity_scores(x) # get coef
print(analyze)
print(type(analyze))

# access compound key of dict
compound = analyze['compound']
print(compound)

# output message
if compound > 0:
    print('Positive')
else:
    print('Negative')

