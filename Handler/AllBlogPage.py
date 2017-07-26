from Handler import Handler
from google.appengine.ext import db
from Model.Comment import Comment
from Model.Message import Message

class AllBlogPage(Handler):
    def get(self):
        user=self.check_login()
        messages=db.GqlQuery("SELECT * FROM Message ORDER BY created DESC LIMIT 10")
        comments={}
        for message in messages:
            q_s=str(message.key().id())
            q_i=message.key().id()
            comment=db.GqlQuery("SELECT * FROM Comment WHERE blog_id='%s' ORDER BY created DESC"%q_s)
            comments[q_i]=comment
        
        self.render("result.html", user = user, messages=messages, comments=comments, error="")
        
    def post(self):
        user=self.check_login()
        if user=="guest" or user==None:
            self.redirect("/blog/login")
            return
        error=""

        #delete comment
        Delete_c = self.request.get_all("delete_c")
        for delete in Delete_c:
            entity=Comment.get_by_id(int(delete))
            if not entity:
                error="Error: No comment to be deleted!"
            elif user==entity.commenter:
                entity.delete()
            else:
                error="Error: You can't delete others' post!"
        #delete blog
        Delete = self.request.get_all("delete")
        for delete in Delete:
            entity=Message.get_by_id(int(delete))
            if not entity:
                error="Error: No blog to be deleted!"
            elif user==entity.author:
                entity.delete()
            else:
                error="Error: You can't delete others' post!"
        
        #like blog
        Like= self.request.get_all("like")
        for like in Like:
            entity=Message.get_by_id(int(like))
            if user==entity.author:
                error="Error: You can't like your own post!"
            else:
                entity.like(user)
        messages=db.GqlQuery("SELECT * FROM Message ORDER BY created DESC LIMIT 10")
        comments={}
        for message in messages:
            q=message.key().id()
            comment=db.GqlQuery("SELECT * FROM Comment WHERE blog_id = '%s' ORDER BY created DESC"%q)
            comments[q]=comment
            
        self.render("result.html", user = user, messages=messages, comments=comments, error=error)
