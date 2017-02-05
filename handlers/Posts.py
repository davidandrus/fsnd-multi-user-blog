from Base import BaseHandler

class PostsHandler(BaseHandler):
    def get(self):
        template_values = {
            'title': 'It Works!'
        }

        self.render('index', template_values)
