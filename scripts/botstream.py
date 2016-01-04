import tweepy,config
from redis import Redis
redis = Redis()

class CustomStreamListener(tweepy.StreamListener):
	def __init__(self,api):
		self.api=api
		super(tweepy.StreamListener, self).__init__()

	def on_status(self, status):
		print(status.text)

	def on_error(self, status_code):
	    print 'error',status_code
	    return False

if __name__ == "__main__":
	auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
	auth.set_access_token(config.access_token, config.access_token_secret)
	api = tweepy.API(auth)
	myStream = tweepy.Stream(auth, CustomStreamListener(api))
	myStream.sample()
	#myStream.filter(track=['aleupbot'])