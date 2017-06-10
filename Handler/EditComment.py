from Model.Comment import Comment
from Handler import Handler
from Model.Message import Message

class EditComment(Handler):
    def get(self, comment_id):
        user=self.check_login()
        if user=="guest" or user==None:
            self.redirect("/blog/login")
        comment=Comment.get_by_id(int(comment_id))
        if not comment:
            return self.error(404)
        if user!=comment.commenter:
            self.redirect("/blog")
        else:
            old_text=comment.text
            original_post=Message.get_by_id(int(comment.blog_id))
            self.render("editcomment.html", user=user, original_post=original_post, old_text=old_text, error="")
    def post(self, comment_id):
        #edit comment
        user=self.check_login()
        if user=="guest" or user==None:
            self.redirect("/blog/login")
        comment=Comment.get_by_id(int(comment_id))
        if not comment:
            return self.error(404)
        if user!=comment.commenter:
            self.redirect("/blog")
        text=self.request.get("text") 
        blog_id=comment.blog_id
        original_post=Message.get_by_id(int(comment.blog_id))
        if  text=="":
            error="Please input some word to modify!"
            self.render("editcomment.html", original_post=original_post, user=user, old_text=text, error=error)
        else:
            comment.modify(text=text)
            self.redirect("/blog/"+blog_id)