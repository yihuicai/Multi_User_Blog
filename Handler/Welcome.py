from Handler import Handler
class Welcome(Handler):
    
    def get(self):
        user=self.check_login()
        if user=="guest" or user==None:
            self.redirect("/blog/login")
        else:
            self.render("welcome.html", user = user)
