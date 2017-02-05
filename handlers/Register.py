from Base import BaseHandler
from models.User import User

class RegisterHandler(BaseHandler):

    def get(self):
        template_vars = {}
        template_vars['errors'] = {}
        template_vars['values'] = {}

        self.render('register.html.j2', template_vars)

    def post(self):
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
            # TODO check for validity of email, send error if invalid format
            template_vars['values']['email'] = email

        # if there are no errors add new user then redirect to front page
        if len(template_vars['errors']) == 0:
            user = User(username=username, password=password, email=email)
            user.put()
            self.redirect("/")

        self.render('register.html.j2', template_vars)
