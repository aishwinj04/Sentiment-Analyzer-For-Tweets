import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as df


def get_tweet(term):

    matched_tweets = []
    tweets = nltk.corpus.twitter_samples.strings()
    for tweet in tweets:
        if term.lower() in tweet.lower():
            matched_tweets.append(tweet)

    return matched_tweets


tweets_list = get_tweet('apple')
series = df.Series(tweets_list)
# print(series)


def analyzer(series):
    analyzer = SentimentIntensityAnalyzer()
    compound_list = []
    for tweet in series:
        analyze = analyzer.polarity_scores(tweet)
        compound = analyze['compound']
        compound_list.append(compound)
    
    return compound_list


lst = analyzer(series)
print(lst)


def check_score(compound_list, length):
    total = 0
    for compound in compound_list:
        total += compound

    return total


value = check_score(lst, len(series))
print(value)
if ()
   

# analyzer = SentimentIntensityAnalyzer()

# text1 = 'Hey, what a beautiful day! How amazing it is!'
# analyze = analyzer.polarity_scores(text1) # get coef
# print(analyze)
# print(type(analyze))

# # access compound key of dict
# compound = analyze['compound']
# print(compound)

# # output message
# if compound > 0:
#     print('Positive')
# else:
#     print('Negative')

