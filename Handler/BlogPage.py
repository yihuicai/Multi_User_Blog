from Model.Message import Message
from Handler import Handler
from google.appengine.ext import db


class BlogPage(Handler):    #The Handler may be invalid
    def get(self, blog_id):
        user=self.check_login()
        #if user=="guest" or user==None:
        #    self.redirect("/blog/login")
        #self.init_comment()
        comment=db.GqlQuery("SELECT * FROM Comment WHERE blog_id='%s' ORDER BY created DESC"%blog_id)
        q_i=int(blog_id)
        comments={}
        comments[q_i]=comment
        result=Message.get_by_id(int(blog_id))
        if not result:
            return self.error(404)
        self.render("result2.html", user=user, messages = result, comments=comments)
        
    def post(self, blog_id):
        user=self.check_login()
        if user=="guest" or user==None:
            self.redirect("/blog/login")
        result=Message.get_by_id(int(blog_id))
        if not result:
            return self.error(404)
        comments=db.GqlQuery("SELECT * FROM Comment WHERE blog_id='%s' ORDER BY created DESC"%blog_id)
        new_like=self.request.get("like")
        if new_like:
            result.like(new_like)
        self.render("result2.html",  user=user, messages=result, comments=comments )
        