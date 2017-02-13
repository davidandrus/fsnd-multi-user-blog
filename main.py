"""
Start App Engine Routes
"""

# https://blog.abahgat.com/2013/01/07/user-authentication-with-webapp2-on-google-app-engine/
# https://github.com/BlackrockDigital/startbootstrap-clean-blog

import webapp2
from handlers.Posts import PostsHandler
from handlers.Register import RegisterHandler
from handlers.Login import LoginHandler
from handlers.Post import PostNewHandler, PostViewHandler, PostDeleteHandler, PostEditHandler


app = webapp2.WSGIApplication([
    (r'/', PostsHandler),
    (r'/register', RegisterHandler),
    (r'/login', LoginHandler),
    (r'/post/new', PostNewHandler),
    (r'/post/(\d+)', PostViewHandler),
    (r'/post/\d+/delete', PostDeleteHandler),
    (r'/post/\d+/edit', PostEditHandler)
    #posts
    #post/view
    #post/edit
    #post/add
    #post/like
    #post/unlike
    #post/addcomment
    #post/edit
    #post/deletecomment
], debug=True)
