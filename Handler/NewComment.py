from Handler import Handler
from Model.Message import Message
from Model.Comment import Comment

class NewComment(Handler):
    def get(self,blog_id):
        user=self.check_login()
        if user=="guest" or user==None:
            self.redirect("/blog/login")
        original_post=Message.get_by_id(int(blog_id))
        if not original_post:
            return self.error(404)
        self.render("newcomment.html", user=user, original_post=original_post)
            
    def post(self,blog_id):
        user=self.check_login()
        if user=="guest" or user==None:
            self.redirect("/blog/login")
        original_post=Message.get_by_id(int(blog_id))
        if not original_post:
            return self.error(404)
        old_text=self.request.get("text")
        if old_text:
            new_comment=Comment(blog_id=blog_id, commenter=user, text=old_text)
            new_comment.put()
            self.redirect("/blog/"+blog_id)
        self.render("newcomment.html", user=user, original_post=original_post, text=old_text, error="Please give a comment!")
