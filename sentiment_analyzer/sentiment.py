from nltk.sentiment import SentimentIntensityAnalyzer


sia = SentimentIntensityAnalyzer()
grades = []

def sentiment_analysis():

    with open('sentiment_analyzer/tweets.txt') as f:
        for tweet in f:
            grades.append(sia.polarity_scores(tweet)['compound'])

    # catches division by zero before it happens
    if len(grades) == 0:
        print('LOL you fucked up your tweet writer')
        print('Anyway just take a 50% because I\'m lazy')
        return 50.63
              
    # returned polarity score
    else:
        initial_average = sum(grades) / len(grades)
              
        try:
            adjusted_average = ((initial_average + 1) / 2) * 100
            open('sentiment_analyzer/tweets.txt', 'w').close()
              
            return adjusted_average

        # if an error is thrown, likely means my math fucked up somewhere and I managed to round a number to zero
        # assuming this to be the case, the only possible scenario this happens is a true 0% compound score
        except:
            print('adjusted average equates to zero. Everyone is having a very bad day.')
            open('sentiment/tweets.txt', 'w').close()
              
            return 0.00
