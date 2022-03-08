from weather_module.weather_tweets import too_cold, below_twenty, below_forty, below_sixty, below_eighty, below_hundred, too_hot
from weather_module.weather_interpreter import daily_weather
import schedule, time, random, tweepy, os

# quick setting of env variables and authentication
consumer_key = os.environ.get('ratio_bot_consumer')
consumer_key_secret = os.environ.get('ratio_bot_consumer_secret')
access_token = os.environ.get('ratio_bot_access')
access_token_secret = os.environ.get('ratio_bot_access_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# collects weather information, fetches a random phrase based on weather conditions,
# posts a tweet that includes a temp, 'real feel temp', and the phrase in question
def daily_weather():

    temp, feels_like = weather_collector()
    
    if feels_like < 0:
        rand = random.SystemRandom().randint(0,6)
        phrase = too_cold[rand]
    elif feels_like < 20:
        rand = random.SystemRandom().randint(0,6)
        phrase = below_twenty[rand]
    elif feels_like < 40:
        rand = random.SystemRandom().randint(0,7)
        phrase = below_forty[rand]
    elif feels_like < 60:
        rand = random.SystemRandom().randint(0,6)
        phrase = below_sixty[rand]
    elif feels_like < 80:
        rand = random.SystemRandom().randint(0,6)
        phrase = below_eighty[rand]
    elif feels_like < 100:
        rand = random.SystemRandom().randint(0,6)
        phrase = below_hundred[rand]
    elif feels_like >= 100:
        rand = random.SystemRandom().randint(0,6)
        phrase = too_hot[random.Random]
    else:
        print('Some error in fetching phrase good goin\' bro')
        phrase = ''
    
    daily = api.update_status(f'Good morning *place*! It\'s currently {temp}°, and it feels like {feels_like}°!\n\n{phrase}\n')
    print(f'Daily Weather tweet sent   ::   {daily.text}')

    # ensures the scheduler is cancelled after the job is fulfilled
    return schedule.CancelJob
    

# scheduler for the weather tweets
def weather_tweet_scheduler():
    print('Weather scheduler starts!')
    schedule.every().day.at('08:00').do(daily_weather)

    # alerts once tweets has been sent
    while True:
        schedule.run_pending()
        time.sleep(5)

        if not schedule.jobs:
            print('\n-------------------------------\nWeather Tweet sent successfully!\n-------------------------------\n')

            # restart the scheduler 
            # I believe decoraters would be a better solution for this
            # but for now brain says ez pz time for bed
            weather_tweet_scheduler()
