from google.appengine.ext import db
import re

class Message(db.Model):   
    '''
    This class define a typical message data structure in database model
    '''
    title = db.StringProperty(required=True)
    author= db.StringProperty(required=False)
    text=db.TextProperty(required=True)
    created=db.DateTimeProperty(auto_now_add=True)
    likes= db.StringProperty(required=False)
    def like(self, liker):
        liker += ", "
        self.likes=str(self.likes)
        if self.likes.find(liker)!=-1:
            self.likes=re.sub(liker,"", self.likes)
        else:
            self.likes = self.likes + liker
        self.put()
        
    def modify(self, title, text):
        self.title = title
        self.text = text
        self.put()
        