from Base import BaseHandler

class PostViewHandler(BaseHandler):
    def get(self):
        self.render('index', {'title': 'Post View'})

class PostAddHandler(BaseHandler):
    def get(self):
        self.render('index', {'title': 'Post Add'})

class PostEditHandler(BaseHandler):
    def get(self):
        self.render('index', {'title': 'Post Edit'})

class PostDeleteHandler(BaseHandler):
    def get(self):
        self.render('index', {'title': 'Post Delete'})
