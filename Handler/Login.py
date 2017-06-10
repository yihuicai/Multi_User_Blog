from Handler import Handler
from google.appengine.ext import db

class Login(Handler):
    def get(self):
        self.render("signin.html", login=False, user="guest", error="")
    def post(self):
        # username verification
        self.init_account()
        username=self.request.get("username")
        password=self.request.get("password")
        users=db.GqlQuery("SELECT * FROM Account")
        valid=False
        true_pw=""
        for user in users:
            if self.auth(username, password, user)==True:
                valid=True
                true_pw=user.password   
                break
        if valid==True:
            password=true_pw
            self.set_cookie(username, password)
            self.redirect("/blog/welcome")
        else:
            error="Invalid login"
            self.render("signin.html", user="guest", oldname=username, error=error)