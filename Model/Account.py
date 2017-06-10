from google.appengine.ext import db


class Account(db.Model):
    '''
    This class define a typical user account data structure in database model
    '''
    username=db.StringProperty(required=True)
    password=db.StringProperty(required=True)
    email=db.StringProperty()
    created=db.DateTimeProperty(auto_now_add=True)