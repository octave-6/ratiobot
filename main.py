from ratio import wordle_ratio_list, ratio_list, ricardo
import tweepy, random, time, os

# setting env variables
consumer_key = os.environ.get('ratio_consumer')
consumer_key_secret = os.environ.get('ratio_consumer_secret')
access_token = os.environ.get('ratio_access')
access_token_secret = os.environ.get('ratio_access_secret')
# setting mantinus twitter ID
# additional IDs can be added for more ratio goodness
mantinus_id = ['ID',]

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
        print('...:::Stalker activated:::...')
        print(ricardo)

    def on_status(self, status):
        '''
        Awaits for tweets from mantinus himself, or other users indicated in list mantinus_id
        '''

        # will @ the RTer with an empty tweet unless caught in this if statement:
        if status.text.startswith('RT'):
            return "Repeat after me: I will not ratio RTs"
        # status.user.id == user ID of the bot posting the ratios,
        # else the bot will endlessly ratio itself
        if status.user.id == 'ID':
            return 'Repeat after me: I will not ratio myself'
        
        # now we can begin the ratio
        else:
            print(f'Tweet from {status.user.screen_name} received:')
            time.sleep(0.6)
            print(status.text, '  ::  ', status.id)
            time.sleep(0.2)
            print('. . . . . .')

            # if Wordle tweet, special ratios are utilized for a more personal experience
            # else, a standard ratio is used
            if status.text.startswith('Wordle'):
                rand = random.randint(0,11)
                api.update_status(f'@{status.user.screen_name} {wordle_ratio_list[rand]}', in_reply_to_status_id=status.id)
                api.create_favorite(status.id)
                time.sleep(1)
                print('wordle ratio sent')

            else:
                rand = random.randint(0,19)
                ratio = api.update_status(f'@{status.user.screen_name} {ratio_list[rand]}', in_reply_to_status_id=status.id)
                print(ratio.id)
                api.create_favorite(ratio.id)
                time.sleep(1)
                print('ratio sent.')


if __name__ == '__main__':
    matninus_listener = Stalker(
        consumer_key, consumer_key_secret,
        access_token, access_token_secret
    )

    matninus_listener.filter(follow=mantinus_id, threaded=True)
