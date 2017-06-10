from Handler import Handler
from Model.Message import Message

class EditBlog(Handler):
    def get(self, blog_id):
        user=self.check_login()
        if user=="guest" or user==None:
            self.redirect("/blog/login")
            return
        blogs=Message.get_by_id(int(blog_id))
        if not blogs:
            return self.error(404)
        if user!=blogs.author:
            self.redirect("/blog")
        else:
            title=blogs.title
            text=blogs.text
            self.render("editblog.html", user=user, old_title=title, old_text=text, error="")
    def post(self, blog_id):
        #edit blog
        user=self.check_login()
        if user=="guest" or user==None:
            self.redirect("/blog/login")
            return
        entity=Message.get_by_id(int(blog_id))
        if not entity:
            return self.error(404)
        if user!=entity.author:
            self.redirect("/blog")
        title=self.request.get("title")
        text=self.request.get("text") 
        if title=="" or text=="":
            error="Please input some word to modify!"
            self.render("editblog.html", user=user, old_title=title, old_text=text, error=error)
        else:
            entity.modify(title=title, text=text)
            self.redirect("/blog/"+blog_id)
        