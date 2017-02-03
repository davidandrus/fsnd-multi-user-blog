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
        self.response.write(template.render({}))

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
        else:
            # test if username exists in db
            template_vars['values']['username'] = username

        if not password:
            template_vars['errors']['password'] = 'Password is required'

        if not password_verify:
            template_vars['errors']['password_verify'] = 'You must verify your password'

        if password and password_verify and password_verify != password:
            template_vars['errors']['password_verify'] = 'Passwords dont match'

        # validate email format

        if email:
            template_vars['values']['email'] = email

        if len(template_vars['errors'].length) === 0:
            # add new record

        self.response.write(template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/register', RegisterHandler)
], debug=True)
