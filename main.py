from sentiment_module import sentiment_scheduler
from weather_module import weather_scheduler
from keywords import *
from ratio import *
from threading import Thread
from datetime import datetime
import tweepy, random, time, os

# setting env variables
consumer_key = os.environ.get('ratio_bot_consumer')
consumer_key_secret = os.environ.get('ratio_bot_consumer_secret')
access_token = os.environ.get('ratio_bot_access')
access_token_secret = os.environ.get('ratio_bot_access_secret')

# users to be followed in the stream for tweet collection are set here
# IDs that are privated will no longer be collected, but will not break the bot thanks to a try/catch block
mantinus_id = [

    ]

# users to be actively ratio'd are set here
ratio_users = [

]

# twitter auth
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

class Stalker(tweepy.Stream):

    def on_connect(self):
        '''
        Timestamps bot startup for downtime checking
        bonus meme ricardo
        '''

        now = datetime.now()
        timestamp = now.strftime("%H:%M:%S")

        with open('connection_log.txt', 'a') as f:
            f.write(f'connection time: {timestamp}\n')
            f.close()

        print('\n...:::Stalker activated:::...')
        print(ricardo)

    def on_connection_error(self):
        '''
        Collects timestamp to measure downtime
        '''

        now = datetime.now()
        timestamp = now.strftime("%H:%M:%S")

        with open('connection_log.txt', 'a') as f:
            f.write(f'disconnect time: {timestamp}\n')
            f.close()
        
        print('Ratiobot connection error. Timestamp stored.')

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
        if str(status.user.id) not in ratio_users:
            try:
                with open('sentiment_module/tweets.txt', 'a') as f:
                    f.write(f'{status.text}\n')
                    print(f'::: :::: :::: :::: :::: :::\nNon-ratio\'d tweet caught and written for SIA by user: {status.user.screen_name}')
                    time.sleep(0.6)
                    print('::: :::: :::: :::: :::: :::\n', status.created_at, status.text)
                    f.close()
            except Exception as e:
                print('non-ratio\'d tweet caught, but error from text writer:')
                print(e)

        else:
            try:
                print(f'::: :::: :::: :::: :::: :::\nTweet from {status.user.screen_name} received:')
                time.sleep(0.6)
                print('::: :::: :::: :::: :::: :::\n', status.created_at, status.text)
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
                legit_RNG = random.SystemRandom().randint(1,10)
                print('RNG:', legit_RNG)
                
                # ratio begins within this if branch
                if legit_RNG < 8:
                    print('Ratio will begin')
                    time.sleep(2)
                    
                    # NOTE: BE AWARE OF THE HIERARCHY
                    # Only ONE ratio can be used, so once a condition is satisfied, the ratio list is picked
                    # therefore, higher priority or special case ratios should be placed first,
                    # user specific ratios should be placed near the end of the conditions
#------------------------------------------------------------------BOT RESPONSES------------------------------------------------------------------#
                    # high proriety functions or features
                    # will execute regardless of other keywords said
                    if 'palette' in status.text.lower() and 'color' in status.text.lower() and any(word in status.text.lower() for word in ratio_bot_keywords):
                        print('attempting to generate a palette...')
                        # generate_function()
                        time.sleep(1)
                        print('We pogging\n')
                    # various one-off customized responses, highly specific
                    # high priority tweets or ratios
                    if status.text.startswith('Wordle'):
                        print('Attempting Wordle ratio. . .')
                        rand = random.SystemRandom().randint(0,9)
                        ratio = api.update_status(f'{wordle_ratio_list[rand]}', in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                        api.create_favorite(ratio.id)
                        time.sleep(1)
                        print(f'wordle ratio sent  ::  {ratio.text}\n')
                    
                    elif 'fortnite' in status.text.lower():
                        print('Attempting fortnite. . .')
                        fortnite = api.update_status(
                            'We got a number one Victory Royale\nYeah, Fortnite, we \'bout to get down (get down)\nTen kills on the board right now\nJust wiped out Tomato Town', 
                            in_reply_to_status_id=status.id, auto_populate_reply_metadata=True
                        )
                        api.create_favorite(fortnite.id)
                        time.sleep(1)
                        print(f'ChugJug with You\n')
                    
                    elif 'steak' in status.text.lower():
                        print('Attempting steak. . .')
                        steak = api.update_status(
                            'Medium Rare steak is superior (Rare if you cook it yourself)\nAnything above medium is unacceptable and your opinion is objectively wrong if you think otherwise', 
                            in_reply_to_status_id=status.id, auto_populate_reply_metadata=True
                        )
                        api.create_favorite(steak.id)
                        time.sleep(1)
                        print('Rare steak is best\n')

                    # this section checks for words in a tweet that overlaps with any lists from keywords.py
                    # medium priority tweets or ratios, more broad conditional set
                    elif any(word in status.text.lower() for word in ratio_bot_keywords):
                        print('Beetlejuice Beetlejuice Beetlejuice')
                        rand = random.SystemRandom().randint(0,5)
                        ratio = api.update_status(f'{say_my_name[rand]}', in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                        api.create_favorite(ratio.id)
                        time.sleep(1)
                        print('say my name')

                    elif any(word in status.text.lower() for word in luke_keywords):
                        print('Attempting Luke. . .')
                        lucas_deist = r'\photos\luke_deist.jpg'
                        api.update_status_with_media(status='luuuuuuuuke', filename=lucas_deist, in_reply_to_status_id=status.id)
                        api.create_favorite(lucas_deist.id)
                        time.sleep(1)
                        print('Luuuuuke')

                    elif any(word in status.text.lower() for word in iup_keywords):
                        print('Attempting IUP ratio. . .')
                        rand = random.SystemRandom().randint(0,5)
                        ratio = api.update_status(f'{iup_ratio_list[rand]}', in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                        api.create_favorite(ratio.id)
                        time.sleep(1)
                        print(f'IUP ratio sent  ::  {ratio.text}\n')

                    elif any(word in status.text.lower() for word in ratio_keywords):
                        print('Attempting ratio ratio. . .')
                        rand = random.SystemRandom().randint(0,5)
                        ratio = api.update_status(f'{ratio_ratio_list[rand]}', in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                        api.create_favorite(ratio.id)
                        time.sleep(1)
                        print(f'Ratio ratio sent  ::  {ratio.text}\n')

                    elif any(word in status.text.lower() for word in cogswell_keywords):
                        print('Attempting Cogswell Ratio. . .')
                        rand = random.SystemRandom().randint(0,5)
                        api.update_status(f'{cogswell_ratio_list[rand]}', in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                        api.create_favorite(ratio.id)
                        time.sleep(1)
                        print(f'Ratio ratio sent  ::  {ratio.text}\n')

                    elif any(word in status.text.lower() for word in ukraine_keywords):
                        print('Attempting to stand with ukraine. . .')
                        api.update_status(f'#StandWithUkraine Donate if you can!\n\nhttps://www.icrc.org/en/donate/ukraine', in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                        print('I Stand with Ukraine\n')

                    # user specific ratios
                    # lower priority as this is as broad a condition as you can get essentially
                    # use liberally, as these may heavily override the general ratios list
                    elif str(status.user.id) == '1255918410': # elizabeth st. nicholas muchesko

                        # three split choices to maximize liz embarrassment
                        liz_RNG = random.SystemRandom().randint(1,6)
                        print('liz RNG:', liz_RNG)

                        # 1/3 chance of specialized liz ratio
                        if liz_RNG <= 2:
                            print('Attempting liz ratio. . .')
                            rand = random.SystemRandom().randint(0,12)
                            ratio = api.update_status(f'{liz_ratios[rand]}', in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                            api.create_favorite(ratio.id)
                            time.sleep(1)
                            print(f'Liz ratio sent  ::  {ratio.text}\n')

                        # 1/6 chance of a silly goofy mood
                        elif liz_RNG == 3:
                            print('Attempting silly goofy mood. . .')
                            rand = random.SystemRandom().randint(0,28)
                            silly_liz = f'photos/liz/liz_{rand}.jpg'
                            embarrassment = api.update_status_with_media(status="@unofficialliz i'M In a SiLlY goOfy mOoD", filename=silly_liz, in_reply_to_status_id=status.id)
                            api.create_favorite(embarrassment.id)
                            time.sleep(1)
                            print('SILLY GOOFY MOOD')
                            
                        # 1/2 chance to use a standard ratio instead
                        # standard ratio has to be created here due to the elif conditions
                        # maybe functions would simplify this but oh well (laughs in Ctrl + C, Ctrl + V)
                        else:
                            rand = random.SystemRandom().randint(0,27)
                            ratio = api.update_status(f'{ratio_list[rand]}', in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                            api.create_favorite(ratio.id)
                            time.sleep(1)
                            print(f'Standard ratio sent  ::  {ratio.text}\n')
                    
                    elif str(status.user.id) == '701177228613316608': # flerb mcgerb
                        fmg_RNG = random.randint(1,6)
                        print('flerb RNG:',fmg_RNG)

                        # 2/3 chance to do nothing
                        # this will prevent the bot from beeing TOO annoying
                        if fmg_RNG <= 4:
                            print('FMG tweet check failed')
                            pass
                        else:
                            print('Attempting flerb to mcgerb')
                            rand = random.SystemRandom().randint(0,14)
                            api.update_status(f'{flerb[rand]}', in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                            time.sleep(1)
                            print('flerb sent to mcgerb')
                        
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

    # simple module loading
    # some modules just get too damn annoying
    grade_tweets = True
    daily_weather = True
    palette_generator = True

    time.sleep(5)

    # loads selected modules
    if grade_tweets == True:
        try:
            Thread(target = sentiment_scheduler.graded_tweet_scheduler).start()

            time.sleep(1)
            print('Initiating Sentiment Analysis module. . .')
            sentiment_online = True
        except Exception as e:
            sentiment_online = False

            time.sleep(2)
        
    if daily_weather == True:
        try:
            Thread(target = weather_scheduler.weather_tweet_scheduler).start()

            time.sleep(1)
            print('Initiating Weather module. . .')
            weather_online = True
        except Exception as e:
            weather_online = False

            time.sleep(2)
        
    # if palette_generator == True:
    #     try:
    #         Thread(target = palette_module.)
    
    time.sleep(4)
    if sentiment_online == True and weather_online == True:
        print('All modules loaded successfully, ratiobot is online')
    
    elif sentiment_online == False:
        print('Ratiobot launched, but the sentiment analysis failed to load. . .')
    elif weather_online == False:
        print('Ratiobot launched, but the daily weather module failed to load. . .')
    
    else:
        print('All modules failed to launch. Ratiobot is fucked.')
