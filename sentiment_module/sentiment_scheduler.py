from sentiment_module.sentiment_analyzer import sentiment_analysis
import schedule, time, random, tweepy, os

# quick setting of env variables and authentication
consumer_key = os.environ.get('ratio_bot_consumer')
consumer_key_secret = os.environ.get('ratio_bot_consumer_secret')
access_token = os.environ.get('ratio_bot_access')
access_token_secret = os.environ.get('ratio_bot_access_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# function for fetching the sentiment from the sentiment analyzer,
# then declares where to pull accompanying tweet from
def graded_tweets():
    print('IT\'S TWEET GRADING TIME')
    cogswell_grade = sentiment_analysis()
    time.sleep(1)
    print(f'Grade: {cogswell_grade}')
    time.sleep(1)

    # unnecessarily large if/elif block begins
    if cogswell_grade < 0:
        print('Error in graded_tweets calculation')
        phrase = 'confused?'
    elif cogswell_grade <= 10:
        phrase = 'super-ultra-depression'
    elif cogswell_grade <= 25:
        phrase = 'depression'
    elif cogswell_grade <= 40:
        phrase = 'sad :('
    elif cogswell_grade <= 60:
        phrase = 'Neutral'
    elif cogswell_grade <= 75:
        phrase = 'Positive :)'
    elif cogswell_grade <= 90:
        phrase = 'Happy!'
    else:
        phrase = 'Fucking-Elated!?'
    
    daily = api.update_status(f'If I could use one word to describe Cogswell Twitter\'s mood this week, it would be:\n\n{phrase}')
    print(f'Daily Grading tweet sent   ::   {daily.text}')

    with open('sentiment_module/grades.txt', 'a') as f:
        f.write(f'{cogswell_grade}\n')
        f.close()

    # ensures the scheduler is cancelled after the job is fulfilled
    return schedule.CancelJob

# scheduler for daily grader tweets
# set currently for 8:30PM
def graded_tweet_scheduler():
    schedule.every().friday.at('20:30').do(graded_tweets)

    # alerts once the tweet has been sent
    while True:
        schedule.run_pending()
        time.sleep(5)