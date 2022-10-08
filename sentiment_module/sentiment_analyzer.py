from nltk.sentiment import SentimentIntensityAnalyzer

# filters junk out of each tweet
# such as @s, https, and hashtags
def filter():
    dirty_tweets = []
    clean_tweets = []

    with open('sentiment_module/tweets.txt', encoding='UTF-8') as f:
        for tweet in f:
            dirty_tweets.append(tweet)
        f.close()
        
    for tweet in dirty_tweets:
            words = str(tweet).split(' ')
            cleaning = [word for word in words if not word.startswith('#') and not word.startswith('http') 
                                                        and not word.startswith('@') and not word.startswith('\n')]
            tweet = ' '.join(cleaning)
            clean_tweets.append(tweet)
    
    return clean_tweets
    
# uses nltk vader model to grade tweet sentiment, then return the score as a float
# default model is trained for social media analysis
def sentiment_analysis():
    sia = SentimentIntensityAnalyzer()
    filtered_tweets = filter()
    grades = []

    for tweet in filtered_tweets:
        grades.append(sia.polarity_scores(tweet)['compound'])

    # catches division by zero before it happens
    print('Tweets graded:', len(grades))
    if len(grades) == 0:
        print('LOL you fucked up your tweet writer')
        print('Anyway just take a 50% because I\'m lazy')
        return 50.696969 
              
    # returned polarity score
    else:
        initial_average = sum(grades) / len(grades)
              
        try:
            adjusted_average = ((initial_average + 1) / 2) * 100
            open('sentiment_module/tweets.txt', 'w').close()
              
            return adjusted_average

        # if an error is thrown, likely means my math fucked up somewhere and I managed to round a number to zero
        # assuming this to be the case, the only possible scenario this happens is a true 0% compound score
        except:
            print('adjusted average equates to zero. Everyone is having a very bad day.')
            open('sentiment/tweets.txt', 'w').close()
              
            return 0.00