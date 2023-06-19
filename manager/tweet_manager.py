from model.tweet import Tweet

class TweetManager():

    def __init__(self):
        self.tweet_list = []

    def tweet(self, username):
        """
        Tweetする。
        """
        content = input('Tweetを入力してください。: ')
        tweet = Tweet(username, content)
        self.tweet_list.append(tweet)
        print('Tweetしました。')
        print()
    
    def show_tweet(self):
        """
        Tweetを一覧表示する。
        """
        for tweet in self.tweet_list:
            print('ユーザー名: ' + tweet.username)
            print('Tweet: ' + tweet.content)
            print()