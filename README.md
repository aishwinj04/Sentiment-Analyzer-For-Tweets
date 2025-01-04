# Sentiment Analysis of Tweets

This Python program analyzes the sentiment of tweets based on a search term given by user-input. It uses the **VADER Sentiment Analyzer** from the **NLTK** library to classify tweets as **positive**, **negative**, or **neutral** as the response of that term.

## Features

- **Search and Analyze Tweets**: Allows users to search for tweets containing a specific term.
- **Sentiment Analysis**: Analyzes the sentiment of matching tweets and calculates an average sentiment score.
- **Sentiment Classification**: Classifies the sentiment as **Positive**, **Negative**, or **Neutral** based on the score.

## Requirements
Download NLTK Resources: 
- nltk.download('vader_lexicon')
- nltk.download('twitter_samples')


## Example
"Enter search term to match for in tweets:" **Google**
Output: Negative Response (-0.09786666666666666)

#### Sample Tweets Analyzed for **Google**:
- **Tweet 1**: @ Sorry that manage files on external SD card via AirDroid is not supported now (Android 4.4+) :( Google has restricted that.
- **Tweet 2**: @ "We're sorry, but Google Play Music is currently experiencing errors. Please try again in a few minutes."\n\n:(
- **Tweet 3**: RT @: How much have The Daily Telegraph paid to get their anti Ed Miliband screeds on the front page of Google? Or was it Tory…

These tweets are used to compute the sentiment response (positive, negative, or neutral) for the search term **Google**, offering insight into how the public feels about it.
