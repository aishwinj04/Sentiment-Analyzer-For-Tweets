import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

#nltk.download(vader_lexicon)

analyzer = SentimentIntensityAnalyzer()

text1 = 'Hey, what a beautiful day! How amazing it is!'
analyze = analyzer.polarity_scores(text1) # positive/negative coef 
print(analyze)