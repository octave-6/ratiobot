from nltk.sentiment import SentimentIntensityAnalyzer


sia = SentimentIntensityAnalyzer()
grades = []

def sentiment_analysis():

    with open('sentiment/tweets.txt') as f:
        for tweet in f:
            grades.append(sia.polarity_scores(tweet)['compound'])


    # returned polarity score
    initial_average = sum(grades) / len(grades)
    try:
        adjusted_average = ((initial_average + 1) / 2) * 100
        open('sentiment/tweets.txt', 'w').close()
        return adjusted_average
    except:
        print('adjusted average equates to zero. Everyone is having a very bad day.')
        open('sentiment/tweets.txt', 'w').close()
        return 0.00
