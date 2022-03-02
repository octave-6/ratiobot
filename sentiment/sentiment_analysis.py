from nltk.sentiment import SentimentIntensityAnalyzer
import csv

sia = SentimentIntensityAnalyzer()
grades = []

def sentiment_analysis():

    with open('sentiment/tweets.csv') as f:
        reader = csv.reader(f)
        for tweet in reader:
            grades.append(sia.polarity_scores(tweet)['compound'])

    f.close()
    f.truncate()

    return sum(grades) / len(grades)

grade = sentiment_analysis()
