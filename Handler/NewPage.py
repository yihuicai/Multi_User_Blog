from Handler import Handler
from Model.Message import Message

class NewPage(Handler):

    def get(self):
        user=self.check_login()
        if user=="guest" or user==None:
            self.redirect("/blog/login")
        else:
            self.render("blog.html", user=user)
            
    def post(self):
        user=self.check_login()
        if user=="guest" or user==None:
            self.redirect("/blog/login")

        title=self.request.get("subject")
        text=self.request.get("content")
        likes=""
        error=""
        if text and title:
            # Python way to create a object
            blog=Message(title=title, text=text, author=user, likes=likes)
            blog.put()
            blog_id=str(blog.key().id())
            self.redirect("/blog/"+blog_id)
        else:
            error="Please input some text in it"
            self.render('blog.html', user=user,
                        subject=title, 
                        content=text, 
                        error=error)
