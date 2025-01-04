import errno
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def get_tweet(term):

    matched_tweets = []
    tweets = nltk.corpus.twitter_samples.strings()
    for tweet in tweets:
        if term.lower() in tweet.lower():
            matched_tweets.append(tweet)

    return matched_tweets


tweets_list = get_tweet('apple')
print(tweets_list)



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

