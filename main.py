
import webapp2
#import sqlite3
from google.appengine.ext import db
#from Handler.Handler import Handler
from Handler.Login import Login
from Handler.Logout import Logout
from Handler.SignUp import SignUp
from Handler.Welcome import Welcome
from Handler.AllBlogPage import AllBlogPage
from Handler.NewPage import NewPage
from Handler.BlogPage import BlogPage
from Handler.EditBlog import EditBlog
from Handler.NewComment import NewComment
from Handler.EditComment import EditComment


app = webapp2.WSGIApplication([('/blog/login', Login),
                               ('/blog/logout', Logout),
                               ('/blog/signup', SignUp),
                               ('/blog/welcome', Welcome),
                               ('/blog', AllBlogPage), 
                               ('/blog/newpost', NewPage), 
                               (r'/blog/(\d+)', BlogPage),
                               (r'/blog/edit/(\d+)', EditBlog),
                               (r'/blog/newcomment/(\d+)',NewComment),
                               (r'/blog/editcomment/(\d+)',EditComment)],
                                debug=True)
# The URL handling session
