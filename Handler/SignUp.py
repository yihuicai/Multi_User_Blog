from Handler import Handler
import re
from Model.Account import Account

class SignUp(Handler):

    def get(self):
        self.render("signup.html", login=False, user="guest")

    def post(self):
        string1=""
        string2=""
        string3=""
        self.init_account()
        # username verification
        username=""
        username=self.request.get("username")
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        
        if username=="" or USER_RE.match(username)==None:
            string1="That's not a valid username."
        else:
            user_exist=self.check_exist()
            for us in user_exist:
                if us.username==username:
                    string1="Username exists!"
        # password verification
        password1=""
        password2=""
        password1=self.request.get("password")
        password2=self.request.get("verify")
        PASS_RE = re.compile(r"^.{3,20}$")
        if password1=="" or password1!=password2 or PASS_RE.match(password1)==None:
            string2="That wasn't a valid password"

        # email verification
        email=""
        email=self.request.get("email")
        if email:
            EMAIL_RE = re.compile(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$")
            if EMAIL_RE.match(email)==None:
                string3="That's not a valid email"
                
        # push in the database and render the html
        if username and  password1 and string1=="" and string2=="" and string3=="":
            password1=self.make_pw_hash(username,password1)
            ac=Account(username=username, 
                       password=password1, 
                       email=email)
            ac.put()
            # define and send cookie
            self.set_cookie(username, password1)
            self.redirect("/blog/welcome")

        else:
            self.render("signup.html", user="guest",
                        error1=string1,
                        error2=string2,
                        error3=string3,
                        oldname=username,
                        oldemail=email)