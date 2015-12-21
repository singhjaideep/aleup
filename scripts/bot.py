import tweepy
import config

class TwitterAPI:
    def __init__(self):
        consumer_key = config.consumer_key
        consumer_secret = config.consumer_secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = config.access_token
        access_token_secret = config.access_token_secret
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message, tweetid=None):
        self.api.update_status(status=message,in_reply_to_status_id=tweetid)

    def displaytweets(self):
    	for tweet in self.api.home_timeline():
    		print tweet.text

    def getMention(self):
    	for mention in self.api.mentions_timeline(count=1): #For now one
    		return mention.user.screen_name, mention.text, mention.id
    
    def processReply(self, text): #very fuzzy logic
    	#print text
    	if 'help' in text: #assume user asked for help
    		return 'tweet with Resturant Name X/5 rating and short dish to try'
    	elif '/' in text: #assume user is reponding correctly
    		test = text.split(' ')
    		for t in test:
	    		if '/' in t :
	    			rating = t
	    	resturant = ' '.join(test[1:test.index(rating)])

    		return 'Got it! You rated '+resturant+' '+rating+'. Aleup!'
    	else:
    		return 'Can you repeat? I didnt get that'


if __name__ == "__main__":
	twitter = TwitterAPI()
	#twitter.displaytweets()
	userWhoMentioned, tweettext, tweetid = twitter.getMention()
	tosay = twitter.processReply(tweettext)
	twitter.tweet("Hey @"+userWhoMentioned+' ! '+tosay,tweetid)
