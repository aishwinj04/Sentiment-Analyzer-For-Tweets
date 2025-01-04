import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as df


def get_tweet(term):

    matched_tweets = []
    tweets = nltk.corpus.twitter_samples.strings()
    for tweet in tweets:
        if term.lower() in tweet.lower(): # match regardless of case
            matched_tweets.append(tweet)

    return matched_tweets


def analyzer(series):
    analyzer = SentimentIntensityAnalyzer()
    compound_list = []
    for tweet in series:
        analyze = analyzer.polarity_scores(tweet)
        compound = analyze['compound']
        compound_list.append(compound)
    
    return compound_list


def check_score(compound_list):
    total = 0
    for compound in compound_list:
        total += compound

    return total


def main():
    search_term = input('Enter search term to match for in tweets: ')
    matched_tweets = get_tweet(search_term)

    # print(matched_tweets)
    
    if not matched_tweets:
        print('No matching tweet with that term')
    else:
        series = df.Series(matched_tweets)
        df.set_option('display.max_colwidth', None)
        print(series) # for visual
        

        scores = analyzer(series)
        total = check_score(scores)

        # score more than 0 indicates positive outlook 
        if(total > 0):
            print('Positive Response')
        else:
            print('Negative Response')

        # print(total)


if __name__ == '__main__':
    main()



   



