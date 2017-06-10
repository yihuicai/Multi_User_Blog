from google.appengine.ext import db
class Comment(db.Model): 
    blog_id=db.StringProperty(required=True)
    commenter=db.StringProperty(required=True)
    text=db.TextProperty(required=True)
    created=db.DateTimeProperty(auto_now_add=True)
    def modify(self, text):
        self.text = text
        self.put()
