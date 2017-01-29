from tweepy import *
from tweepy.streaming import *
 
 
class TwitterBot(object):
    def __init__(self, ck, cs, at, ats):
        auth = OAuthHandler(ck, cs)
        auth.set_access_token(at, ats)
 
        self.api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
 
    def reply(self, message, twt_id):
        self.api.update_status(message, twt_id)
        print 'Replied.'
 
 
class Listener(StreamListener):
    def __init__(self, twitter_bot, username, keyword, reply):
        super(Listener, self).__init__()
        self.twitter_bot = twitter_bot
        self.username = username.lower()
        self.keyword = keyword.lower()
        self.reply = reply
 
    def on_connect(self):
        print 'Connection established'
 
    def on_disconnect(self, notice):
        print 'Connection lost:', notice
 
    def on_status(self, status):
        username = status.author.screen_name
        if username.lower() == self.username and self.keyword in status.text.lower():
            self.twitter_bot.reply('@{} {}'.format(username, self.reply), status.id)
 
 
norm_ck = 'E5SVEWxo7CS8s1vLKLXP5iDYH'
norm_cs = 'GVzdm1Sf0o8rHRumwzHV1r8mZFwkdCdzk9oaS1F16AXNTSVNaS'
norm_at = '703033969948942337-0KEZH2JMpwNNXQo8M2dSvvDdAevStny'
norm_ats = 'ASf8EGOF2zGumzHTHILc5wZwngtHFbSOOLeMymcEe37DB'
 
handle = raw_input('@adidasoriginals').strip()
keyword = raw_input('boost').strip()
reply = raw_input('not yeezy').strip()
 
twtr_bot = TwitterBot(norm_ck, norm_cs, norm_at, norm_ats)
listener = Listener(twtr_bot, handle, keyword, reply)
stream = Stream(auth=twtr_bot.api.auth, listener=listener)
 
while 1:
    try:
        stream.userstream(_with='followings')
    except KeyboardInterrupt:
        print 'Stopping...'
        break
    except Exception as e:
        print efrom tweepy import *
from tweepy.streaming import *
 
 
class TwitterBot(object):
    def __init__(self, ck, cs, at, ats):
        auth = OAuthHandler(ck, cs)
        auth.set_access_token(at, ats)
 
        self.api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
 
    def reply(self, message, twt_id):
        self.api.update_status(message, twt_id)
        print 'Replied.'
 
 
class Listener(StreamListener):
    def __init__(self, twitter_bot, username, keyword, reply):
        super(Listener, self).__init__()
        self.twitter_bot = twitter_bot
        self.username = username.lower()
        self.keyword = keyword.lower()
        self.reply = reply
 
    def on_connect(self):
        print 'Connection established'
 
    def on_disconnect(self, notice):
        print 'Connection lost:', notice
 
    def on_status(self, status):
        username = status.author.screen_name
        if username.lower() == self.username and self.keyword in status.text.lower():
            self.twitter_bot.reply('@{} {}'.format(username, self.reply), status.id)
 
 
norm_ck = 'E5SVEWxo7CS8s1vLKLXP5iDYH'
norm_cs = 'GVzdm1Sf0o8rHRumwzHV1r8mZFwkdCdzk9oaS1F16AXNTSVNaS'
norm_at = '703033969948942337-0KEZH2JMpwNNXQo8M2dSvvDdAevStny'
norm_ats = 'ASf8EGOF2zGumzHTHILc5wZwngtHFbSOOLeMymcEe37DB'
 
handle = raw_input('@adidasoriginals').strip()
keyword = raw_input(‘boost').strip()
reply = raw_input('not yeezy').strip()
 
twtr_bot = TwitterBot(norm_ck, norm_cs, norm_at, norm_ats)
listener = Listener(twtr_bot, handle, keyword, reply)
stream = Stream(auth=twtr_bot.api.auth, listener=listener)
 
while 1:
    try:
        stream.userstream(_with='followings')
    except KeyboardInterrupt:
        print 'Stopping...'
        break
    except Exception as e:
        print e
