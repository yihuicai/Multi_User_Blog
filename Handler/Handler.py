import os
import jinja2
import random
import hashlib
import webapp2
from Model.Account import Account
from Model.Comment import Comment
from google.appengine.ext import db


template_dir= os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape= True)

            
class Handler(webapp2.RequestHandler):
    
    user="guest"
    
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
        
    #def render_front(self, user, result, blog_id):
        #if blog_id:
            #messages=[]
            #messages.append(result)
        #else:
            #messages=db.GqlQuery("SELECT * FROM Message ORDER BY created DESC LIMIT 10")

        #self.render("result.html",  user=user, messages=messages )

    def init_comment(self):
        init=Comment(blog_id=" ", commenter=" ", text=" ")
        init.put()
    def check_exist(self):
        user_exist=db.GqlQuery("SELECT * FROM Account ORDER BY created DESC")
        return user_exist
        
    def make_salt(self):
        salt=[]
        ret=""
        for i in range (0,5):
            ran=random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
            salt.append(ran)
        ret=ret.join(salt)
        return ret

    def make_pw_hash(self, name, pw):
        salt=self.make_salt()
        ret=hashlib.sha256(name+pw+salt).hexdigest()+"-"+salt
        return ret
    
    def auth(self, name, pw, user):
        pw1=user.password.split("-")[0]
        if pw1==" ":
            return False
        salt=user.password.split("-")[1]
        pw2=hashlib.sha256(name+pw+salt).hexdigest()
        if pw2==pw1:
            return True
        return False
        
    def set_cookie(self, u, p):
        cookie=self.make_pw_hash(u,p)
        self.response.headers.add_header('Set-Cookie', 'name=%s; Path=/'%cookie)

    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'name=; Path=/')
        

        
    def check_login(self):
        # Initialize cookie identifier
        user1=self.request.cookies.get("name")
        salt=""
        key=""
        
        # Make cookie
        if user1==None:
            return "guest"
        s=user1.split("-")
        if s[0]==user1:
            return "guest"
        else:
            salt=s[1]
            key=s[0]
        # Check database, see if there is a match
        user_exist=""
        user2=self.check_exist()
        for user in user2:
            if hashlib.sha256(user.username+user.password+salt).hexdigest()==key:
                user_exist=user.username
        if user_exist=="":
            return "guest"
        else:
            return user_exist
