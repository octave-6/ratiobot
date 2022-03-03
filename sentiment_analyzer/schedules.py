from sentiment_analyzer.sentiment_tweets import *
from sentiment_analyzer.sentiment import sentiment_analysis
import schedule, time, random, tweepy, os

consumer_key = os.environ.get('ratio_bot_consumer')
consumer_key_secret = os.environ.get('ratio_bot_consumer_secret')
access_token = os.environ.get('ratio_bot_access')
access_token_secret = os.environ.get('ratio_bot_access_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

def graded_tweets():
    print('ITS TWEET GRADING TIME')
    cogswell_grade = sentiment_analysis()
    time.sleep(1)
    print(f'Grade: {cogswell_grade}')
    time.sleep(1)

    if cogswell_grade < 0:
        print('Error in graded_tweets calculation')
        return
    if cogswell_grade == 0:
        rand = random.SystemRandom().randint(0,3)
        phrase = zero[rand]
    if cogswell_grade <= 10:
        rand = random.SystemRandom().randint(0,3)
        phrase = ten_and_under[rand]
    elif cogswell_grade <= 20:
        rand = random.SystemRandom().randint(0,5)
        phrase = twenty_and_under[rand]
    elif cogswell_grade <= 30:
        rand = random.SystemRandom().randint(0,5)
        phrase = thirty_and_under[rand]
    elif cogswell_grade <= 40:
        rand = random.SystemRandom().randint(0,5)
        phrase = forty_and_under[rand]
    elif cogswell_grade <= 50:
        rand = random.SystemRandom().randint(0,5)
        phrase = fifty_and_under[rand]
    elif cogswell_grade <= 60:
        rand = random.SystemRandom().randint(0,5)
        phrase = sixty_and_under[rand]
    elif cogswell_grade <= 70:
        rand = random.SystemRandom().randint(0,5)
        phrase = seventy_and_under[rand]
    elif cogswell_grade <= 80:
        rand = random.SystemRandom().randint(0,5)
        phrase = eighty_and_under[rand]
    elif cogswell_grade <= 90:
        rand = random.SystemRandom().randint(0,5)
        phrase = ninety_and_under[rand]
    else:
        rand = random.SystemRandom().randint(0,5)
        phrase = hundred_and_under[rand]
    
    api.update_status(f'The students of Cogswell Hall apear to be {cogswell_grade:.2f}% happy today.\n\n{phrase}')

def graded_scheduler():
    schedule.every().day.at('20:30').do(graded_tweets)

    while True:
        schedule.run_pending()
        if not schedule.jobs:
            print('Graded Tweet sent successfully!')