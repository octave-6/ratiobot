from weather_module.weather_interpreter import weather_collector
import schedule, time, random, tweepy, os

# quick setting of env variables and authentication
consumer_key = os.environ.get('ratio_bot_consumer')
consumer_key_secret = os.environ.get('ratio_bot_consumer_secret')
access_token = os.environ.get('ratio_bot_access')
access_token_secret = os.environ.get('ratio_bot_access_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# dictionaries for translating code to weather
# flavor text is stored in weather_phrases
weather_codes = {
    "01": "with clear skies",
    "02": "and is slightly cloudy",
    "03": "with partial cloud coverage",
    "04": "and is mostly cloudy",
    "09": "with some showers",
    "10": "and is expected to rain",
    "11": "with storms to be expected",
    "13": "with some snow to come our way",
    "50": "expect heavy fog for the day"
}

weather_phrases = {
    "01": "A bright and sunny day!",
    "02": "Enjoy a little break from the sun!",
    "03": "Enjoy a little break from the sun!",
    "04": "Enjoy a little break from the sun!",
    "09": "Nothing wrong with a rainy day every now and then!",
    "10": "Don't forget an umbrella today!",
    "11": "Today's a good day to sit inside and enjoy the atmosphere!",
    "13": "Snow!!!",
    "50": "the mist."
}

# collects weather information, fetches a random phrase based on weather conditions,
# posts a tweet that includes a temp, 'real feel temp', and the phrase in question
def daily_weather():

    temp, condition = weather_collector()

    # collection of weather & phrase from dictionary
    condition_phrase = weather_codes[str(condition[0:2])]
    phrase = weather_phrases[str(condition[0:2])]
    
    daily = api.update_status(f'Goooood morning I-U-People!\n\nIt is currently {str(temp)[0:2]}°F, {condition_phrase}!\n\n{phrase}')
    print(f'Daily Weather tweet sent   ::   {daily.text}')

    # ensures the scheduler is cancelled after the job is fulfilled
    return schedule.CancelJob
    

# scheduler for the weather tweets
def weather_tweet_scheduler():
    schedule.every().day.at('09:00').do(daily_weather)

    # alerts once tweets has been sent
    while True:
        schedule.run_pending()
        time.sleep(5)