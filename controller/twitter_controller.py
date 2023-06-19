from manager.user_manager import UserManager
from manager.tweet_manager import TweetManager

class TwitterController():

    def __init__(self):
        self.user_manager = UserManager()
        self.tweet_manager = TweetManager()
        self.login_username = None

    def controller(self):
        while True:
            print("1.ユーザー登録")
            print("2.ログイン")
            print("3.ログアウト")
            print("4.Tweetする")
            print("5.Tweetを一覧表示する")
            print("6.Twitterを終了する")
            action = input("実行する操作を入力してください。: ")

            if action == "1":
                self.user_manager.register_user()
            elif action == "2":
                self.login_username = self.user_manager.login()
            elif action == "3":
                self.login_username = None
                print('ログアウトしました。')
                print()
            elif action == "4":
                if self.login_username:
                    self.tweet_manager.tweet(self.login_username)
                else:
                    print('ログインしてください。')
                    print()
            elif action == "5":
                self.tweet_manager.show_tweet()
            else:
                print('遊んでくれてありがとう！')
                break