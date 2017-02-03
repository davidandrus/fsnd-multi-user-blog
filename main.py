"""
Start App Engine Routes
"""

import webapp2
import jinja2
from os import path
from google.appengine.ext import ndb

print(ndb)

JINJA_TEMPLATE_PATH = path.join(path.dirname(__file__), 'templates')
JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(JINJA_TEMPLATE_PATH),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class User(ndb.Model):
    username = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    email = ndb.StringProperty()
    password = ndb.StringProperty()
    modified = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def exists(cls, username):
        return cls.query(User.username == username).fetch(1)

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

        template_vars = {}
        template_vars['errors'] = {}
        template_vars['values'] = {}

        self.response.write(template.render(template_vars))

    def post(self):
        template = JINJA_ENV.get_template('register.html.j2')
        username = self.request.get('username').strip()
        password = self.request.get('password').strip()
        password_verify = self.request.get('password-verify').strip()
        email = self.request.get('email').strip()

        template_vars = {}
        template_vars['errors'] = {}
        template_vars['values'] = {}

        if not username:
            template_vars['errors']['username'] = 'Username is required'
        # test if username exists in db
        elif User.exists(username):
            template_vars['errors']['username'] = 'Username is already taken'
        else:
            template_vars['values']['username'] = username

        if not password:
            template_vars['errors']['password'] = 'Password is required'

        if not password_verify:
            template_vars['errors']['password_verify'] = 'You must verify your password'

        if password and password_verify and password_verify != password:
            template_vars['errors']['password_verify'] = 'Passwords dont match'

        if email:
            template_vars['values']['email'] = email

        # if there are no errors add new user then redirect to front page
        if len(template_vars['errors']) == 0:
            user = User(username=username, password=password, email=email)
            user.put()
            self.redirect("/")

        self.response.write(template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/register', RegisterHandler)
], debug=True)
