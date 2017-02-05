from Base import BaseHandler

class MainHandler(BaseHandler):
    def get(self):
        template_values = {
            'title': 'It Works!'
        }

        self.render('index.html.j2', template_values)
