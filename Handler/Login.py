from Handler import Handler
from google.appengine.ext import db

class Login(Handler):
    def get(self):
        self.render("signin.html", login=False, user="guest", error="")
    def post(self):
        # username verification
        username=self.request.get("username")
        password=self.request.get("password")
        users=db.GqlQuery("SELECT * FROM Account")
        true_pw=""
        valid = False
        for user in users:
            if self.auth(username, password, user)==True:
                valid=True
                password=user.password
                self.set_cookie(username, password)
                self.redirect("/blog/welcome")            
                break
        if valid == False:
            error="Invalid login"
            self.render("signin.html", user="guest", oldname=username, error=error)
