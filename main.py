from sentiment_module import sentiment_scheduler
from weather_module import weather_scheduler
from user_lists import *
from keywords import *
from ratio import *
from threading import Thread
from datetime import datetime
import tweepy, random, time, os

# env variables for privacy and twitter auth
consumer_key = os.environ.get('ratio_bot_consumer')
consumer_key_secret = os.environ.get('ratio_bot_consumer_secret')
access_token = os.environ.get('ratio_bot_access')
access_token_secret = os.environ.get('ratio_bot_access_secret')


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
        Collects tweet status from indicated users and immediately records them to tweets.txt
        Indicated users are responded to immediately, allowing optimal ratio time
        '''

        # will @ the RTer with an empty tweet unless caught
        if status.text.startswith('RT'):
            return "Repeat after me: I will not ratio RTs"

        # on status received, writes tweet to sentiment_module/tweets.txt
        # I had previously structured this in a stupid series of if/else statements
        # when I really didn't need to, what can I say, I get paid by each line of code written
        with open('sentiment_module/tweets.txt', 'a', encoding='UTF-8') as f:

            try:
                if status.truncated == True:
                        f.write(status.extended_tweet['full_text'] + '\n')
                        print(f'::: :::: :::: :::: :::: :::\nTweet written to sentiment_module/tweets.txt for sentiment analysis by:\n{status.user.screen_name}')
                        time.sleep(0.6)
                        print('::: :::: :::: :::: :::: :::\n', status.created_at, '\n', status.extended_tweet['full_text'])
                        f.close()
                
                else:
                    f.write(status.text + '\n')
                    print(f'::: :::: :::: :::: :::: :::\nTweet written to sentiment_module/tweets.txt for sentiment analysis by:\n{status.user.screen_name}')
                    time.sleep(0.6)
                    print('::: :::: :::: :::: :::: :::\n', status.created_at, '\n', status.text)
                    f.close()

            except Exception as e:
                print('Error with tweet writing to sentiment_module/tweets.txt:')
                print(e)

                # close /tweets.txt in the event of error
                f.close()
        
        if str(status.user.id) in ratio_users:

            try:
                # standard functions that do not require RNG adjustment go here
                # this would be the palette generator function or !remindme function
                # some forms of ratios also go here since their condition of happening is so incredibly rare to begin with
                if 'palette' in status.text.lower() and 'color' in status.text.lower() and any(word in status.text.lower() for word in ratio_bot_keywords):
                    print('attempting to generate a palette...')
                    # generate_function()
                    time.sleep(1)
                    print('We pogging\n')

                elif status.text.startswith('Wordle'):
                    print('Attempting Wordle ratio. . .')
                    rand = random.SystemRandom().randint(0,9)
                    ratio = api.update_status(f'{wordle_ratio_list[rand]}', in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                    api.create_favorite(ratio.id)
                    time.sleep(1)
                    print(f'wordle ratio sent  ::  {ratio.text}\n')
                

                else:
                    # my bot is really fucking annoying
                    # make it less (or more) annoying here:          
                    legit_RNG = random.SystemRandom().randint(1,100)
                    print('RNG:', legit_RNG)

                    if legit_RNG <= 80:
                        print('Ratio will begin')
                        time.sleep(2)
                        
                        # NOTE: BE AWARE OF THE HIERARCHY
                        # Only ONE ratio can be used, so once a condition is satisfied, the ratio list is picked
                        # therefore, higher priority or special case ratios should be placed first,
                        # user specific ratios should be placed near the end of the conditions
    #------------------------------------------------------------------BOT RESPONSES------------------------------------------------------------------#
                        # high proriety functions or features
                        # will execute regardless of other keywords said
                        
                        if 'fortnite' in status.text.lower():
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
                            rand = random.SystemRandom().randint(0,14)
                            ratio = api.update_status(f'{say_my_name[rand]}', in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                            api.create_favorite(ratio.id)
                            time.sleep(1)
                            print('say my name')

                        elif any(word in status.text.lower() for word in luke_keywords):
                            print('Attempting Luke. . .')
                            lucas_deist = r'/photos/luke_deist.jpg'
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
                            rand = random.SystemRandom().randint(0,6)
                            ratio = api.update_status(f'{ratio_ratio_list[rand]}', in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                            api.create_favorite(ratio.id)
                            time.sleep(1)
                            print(f'Ratio ratio sent  ::  {ratio.text}\n')

                        elif any(word in status.text.lower() for word in cogswell_keywords):
                            print('Attempting Cogswell Ratio. . .')
                            rand = random.SystemRandom().randint(0,7)
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
                                rand = random.SystemRandom().randint(0,17)
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
                                rand = random.SystemRandom().randint(0,32)
                                ratio = api.update_status(f'{ratio_list[rand]}', in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                                api.create_favorite(ratio.id)
                                time.sleep(1)
                                print(f'Standard ratio sent  ::  {ratio.text}\n')
                        
                        elif str(status.user.id) == '701177228613316608': # flerb mcgerb
                            fmg_RNG = random.randint(1,6)
                            print('flerb RNG:',fmg_RNG)

                            # 2/3 chance to do nothing
                            # this will prevent the bot from beeing TOO annoying
                            if fmg_RNG <= 2:
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
                            rand = random.SystemRandom().randint(0,32)
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

    try:
        main()
        print('Ratio bot main funcationality online')

    except Exception as e:
        print('Ratio failed to load')

    # simple module loading
    # some modules just get too damn annoying
    grade_tweets = True
    daily_weather = True
    palette_generator = True

    time.sleep(3)

    # loads selected modules
    if grade_tweets == True:
        try:
            Thread(target = sentiment_scheduler.graded_tweet_scheduler).start()

            time.sleep(1)
            print('Initiating Sentiment Analysis module. . .')
            sentiment_online = True
        except Exception as e:
            sentiment_online = False

            time.sleep(1)
        
    if daily_weather == True:
        try:
            Thread(target = weather_scheduler.weather_tweet_scheduler).start()

            time.sleep(1)
            print('Initiating Weather module. . .')
            weather_online = True
        except Exception as e:
            weather_online = False

            time.sleep(1)
        
    # if palette_generator == True:
    #     try:
    #         Thread(target = palette_module.)
    
    time.sleep(2)
    if sentiment_online == True and weather_online == True:
        print('All modules loaded successfully')
    
    elif sentiment_online == False:
        print('Ratiobot launched, but the sentiment analysis failed to load. . .')
    elif weather_online == False:
        print('Ratiobot launched, but the daily weather module failed to load. . .')
    
    else:
        print('All modules failed to launch. Ratiobot is fucked.')
