from sentiment_module import sentiment_scheduler
from weather_module import weather_scheduler
from keywords import *
from ratio import *
from threading import Thread
import tweepy, random, time, os

# setting env variables
consumer_key = os.environ.get('ratio_bot_consumer')
consumer_key_secret = os.environ.get('ratio_bot_consumer_secret')
access_token = os.environ.get('ratio_bot_access')
access_token_secret = os.environ.get('ratio_bot_access_secret')
# setting mantinus twitter ID
# additional IDs can be added for more ratio goodness
mantinus_id = [
    '855841375094484993', '1389291966458912768', '1454908630617268228', '1292871134212435968',
    '2408557408', '765389324724625408', '1106758045370073098', '1519685210', '1014559035725680640',
    '1360436888214134788', '1127781860149428225', '983030705440555009', '1255918410', '1457952757',
    '1123602921327943681', '905958091887452160', '841776740456402944', '1179080091332206598',
    '1317082603942563843', '1233533606724820992', '701177228613316608', '824021275517521920',
    '2999135039', '1642032943', 
    ]

ratio_users = [
    '1317082603942563843', '1255918410', '701177228613316608', '905958091887452160',
]


# twitter auth
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

class Stalker(tweepy.Stream):

    def on_connect(self):
        '''
        Allows me to ensure bot connected A-Okay,
        Plus bonus meme Ricardo to warm my heart
        '''
        print('\n...:::Stalker activated:::...')
        print(ricardo)

    def on_status(self, status):
        '''
        Awaits for tweets from mantinus himself, or other users indicated in list mantinus_id
        '''

        # will @ the RTer with an empty tweet unless caught
        if status.text.startswith('RT'):
            return "Repeat after me: I will not ratio RTs"
        # ensures the bot doesn't mindlessly ratio everyone, including itself
        # also catches tweets of other users, writes tweets to a txt file
        # for the purpose collecting larger data samples for SIA
        if not str(status.user.id) in ratio_users:
            try:
                with open('sentiment_module/tweets.txt', 'a') as f:
                    f.write(f'{status.text}\n')
                    print('Non-ratio\'d tweet caught and written for SIA')
                    time.sleep(0.2)
                    print(f'Tweet from {status.user.screen_name}:')
                    time.sleep(0.6)
                    print(status.text, '  ::  ', status.id)
                    f.close()
            except Exception as e:
                print('non-ratio\'d tweet caught, but error from text writer:')
                print(e)
            return 'We shall not ratio these, child'

        else:
            try:
                print(f'Tweet from {status.user.screen_name} received:')
                time.sleep(0.6)
                print(status.text, '  ::  ', status.id)
                time.sleep(0.2)
                print('. . . . . .')
                time.sleep(0.5)

                try:
                    with open('sentiment_module/tweets.txt', 'a') as f:
                        f.write(f'{status.text}\n')
                        print('tweet written')
                        f.close()
                except Exception as e:
                    print('Error from text writer:')
                    print(e)

                # my bot is really fucking annoying
                # make it less (or more) annoying here:
                # currently set at: 100% ratio percentage
                legit_RNG = random.SystemRandom().randint(1,1)
                print('RNG:', legit_RNG)
                
                # ratio begins within this if branch
                if legit_RNG == 1:
                    print('Ratio will begin')
                    time.sleep(2)
                    
                    # NOTE: BE AWARE OF THE HIERARCHY
                    # Only ONE ratio can be used, so once a condition is satisfied, the ratio list is picked
                    # therefore, higher priority or special case ratios should be placed first,
                    # user specific ratios should be placed near the end of the conditions

                    # various one-off customized responses, highly specific
                    # high priority tweets or ratios
                    if status.text.startswith('Wordle'):
                        print('Attempting Wordle ratio. . .')
                        rand = random.SystemRandom().randint(0,9)
                        ratio = api.update_status(f'{wordle_ratio_list[rand]}', in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                        api.create_favorite(ratio.id)
                        time.sleep(1)
                        print(f'wordle ratio sent  ::  {ratio.text}\n')
                    
                    # standard ratio is used after all these checks are put in place
                    else:
                        print('Attempting standard ratio. . .')
                        rand = random.SystemRandom().randint(0,27)
                        ratio = api.update_status(f'{ratio_list[rand]}', in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                        api.create_favorite(ratio.id)
                        time.sleep(1)
                        print(f'ratio sent  ::  {ratio.text}\n')


                # this is that RNG else that you probably forgot existed
                else:
                    print('RNG has decided no ratio shall be used today')
                    print('The students of Cogswell are spared, for now...')


            except Exception as e:
                print('yo you suck at writing code:', e)

def main():
    matninus_listener = Stalker(
        consumer_key, consumer_key_secret,
        access_token, access_token_secret,
    )

    matninus_listener.filter(follow=mantinus_id, threaded=True)



if __name__ == '__main__':
    main()

    # simply to confirm the threaded listener class isn't interfering with other tasks somehow
    time.sleep(10)
    try:
        Thread(target = sentiment_scheduler.graded_tweet_scheduler).start()
        Thread(target = weather_scheduler.daily_weather).start()

        time.sleep(1)
        print('RatioBot online and functional')
    except Exception as e:
        print('Error launching RatioBot:', e)
        
        time.sleep(10)
        exit()