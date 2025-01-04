import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as df

# if not locally downloaded uncomment
# nltk.download('vader_lexicon')
# nltk.download('twitter_samples')

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

    average = total/len(compound_list)
    return average


def main():
    search_term = input('Enter search term to match for in tweets: ')
    matched_tweets = get_tweet(search_term)

    # print(matched_tweets)
    
    if not matched_tweets:
        print('No matching tweet with that term')
    else:

        # for organization pandas
        series = df.Series(matched_tweets)
        df.set_option('display.max_colwidth', None)
        # print(series) 

        scores = analyzer(series)
        average = check_score(scores)

        # score more than 0 indicates positive outlook 
        if(average > 0):
            print(f'Positive Response ({average})')
        elif(average < 0):
            print(f'Negative Response ({average})')
        else:
            print(f'Neutral Response ({average})')



if __name__ == '__main__':
    main()



   



