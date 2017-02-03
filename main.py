"""
Start App Engine Routes
"""

import webapp2
import jinja2
from os import path

JINJA_TEMPLATE_PATH = path.join(path.dirname(__file__), 'templates')
JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(JINJA_TEMPLATE_PATH),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'title': 'It Works!'
        }
        template = JINJA_ENV.get_template('index.html.j2')
        self.response.write(template.render(template_values))

class RegisterHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENV.get_template('register.html.j2')
        template_values = {}
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/register', RegisterHandler)
], debug=True)
