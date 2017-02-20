from Base import BaseHandler

from models.Post import Post

class PostViewHandler(BaseHandler):
    def get(self, *args):
        post_id = int(args[0])
        post = Post.get_by_id(post_id)
        errors = {}

        self.render('post', {
            'title': post.title,
            'content': post.content,
            'errors': errors
        })

class PostNewHandler(BaseHandler):
    def get(self):
        template_vars = {}
        template_vars['errors'] = {}
        template_vars['values'] = {}

        self.render('post_add', template_vars)

    def post(self):
        title = self.request.get('title').strip()
        content = self.request.get('content').strip()

        template_vars = {}
        template_vars['errors'] = {}
        template_vars['values'] = {}

        if not title:
            template_vars['errors']['title'] = 'Title is Required'

        if not content:
            template_vars['errors']['content'] = 'Content is Required'

        if len(template_vars['errors']) == 0:
            print 'no errors should create'

            # make post
            post = Post(
                title=title,
                content=content
            )

            # save post
            inserted = post.put()

            # TODO - see if need to handle case where insert fails
            self.redirect('/post/%s' % inserted.id())

        self.render('post_add', template_vars)

class PostEditHandler(BaseHandler):
    def get(self):
        self.render('index', {'title': 'Post Edit'})

class PostDeleteHandler(BaseHandler):
    def get(self):
        self.render('index', {'title': 'Post Delete'})
