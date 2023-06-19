from model.user import User


class UserManager():

    def __init__(self):
        self.user_list = []
    
    def register_user(self):
        """
        ユーザーを登録する。
        同じユーザー名が存在する場合、登録できない。
        """
        username = input('ユーザー名を入力してください。: ')
        password = input('パスワードを入力してください。: ')

        # ユーザー名が既に登録されているかチェックする。
        exist_user = [user for user in self.user_list if user.username == username]

        if exist_user:
            print('ユーザー名が既に登録されています。')
        else:
            user = User(username, password)
            self.user_list.append(user)
            print('ユーザー登録が完了しました。')

        # ユーザーを一覧表示する
        for user in self.user_list:
            print(user.username)
        print()

    def login(self):
        """
        ログインする。
        ユーザー名とパスワードが一致する場合、ログインできる。
        """
        username = input('ユーザー名を入力してください。: ')
        password = input('パスワードを入力してください。: ')

        # ユーザー名が既に登録されているかチェックする。
        loginuser = [user for user in self.user_list if user.username == username]

        if loginuser:
            if loginuser[0].password == password:
                print('ログインしました。')
                print()
                return loginuser[0].username
            else:
                print('ユーザー名またはパスワードが間違っています。')
                print()
        else:
            print('ユーザー名またはパスワードが間違っています。')
            print()
