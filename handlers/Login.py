from Base import BaseHandler

class LoginHandler(BaseHandler):
    def get(self):
        template_vars = {}
        template_vars['errors'] = {}
        self.render('login', template_vars)
