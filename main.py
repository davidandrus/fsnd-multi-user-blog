"""
Start App Engine Routes
"""

import webapp2
from handlers.Register import RegisterHandler
from handlers.Main import MainHandler

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/register', RegisterHandler)
], debug=True)
