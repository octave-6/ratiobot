from ratio import wordle_ratio_list, ratio_list, ricardo
import tweepy, random, time, os

# setting env variables
consumer_key = os.environ.get('ratio_consumer')
consumer_key_secret = os.environ.get('ratio_consumer_secret')
access_token = os.environ.get('ratio_access')
access_token_secret = os.environ.get('ratio_access_secret')
# setting mantinus twitter ID
# additional IDs can be added for more ratio goodness
mantinus_id = ['ID HERE',]

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
        # for some reason user_ids didn't work for me unless they were strings
        # that has since been fixed, but blahblahblah integers are strings now
        if not str(status.user.id) in mantinus_id:
            return 'Ratio responsibly, child'
        
        # now we can begin the ratio
        else:
            try:
                print(f'Tweet from {status.user.screen_name} received:')
                time.sleep(0.6)
                print(status.text, '  ::  ', status.id)
                time.sleep(0.2)
                print('. . . . . .')
                time.sleep(0.5)

                # if Wordle tweet, special ratios are utilized for a more personal experience
                # else, a standard ratio is used
                if status.text.startswith('Wordle'):
                    rand = random.randint(0,11)
                    ratio = api.update_status(f'@{status.user.screen_name} {wordle_ratio_list[rand]}', in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                    api.create_favorite(ratio.id)
                    time.sleep(1)
                    print('wordle ratio sent')
                
                # Add elif conditions here to further personalize your ratio experience
                
                else:
                    rand = random.randint(0,38)
                    ratio = api.update_status(f'@{status.user.screen_name} {ratio_list[rand]}', in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                    api.create_favorite(ratio.id)
                    time.sleep(1)
                    print('ratio sent.')
            except Exception as e:
                print('yo you suck at writing code:', e)

def main():
    matninus_listener = Stalker(
        consumer_key, consumer_key_secret,
        access_token, access_token_secret
    )

    matninus_listener.filter(follow=mantinus_id, threaded=True)


if __name__ == '__main__':
    main()
