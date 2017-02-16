from Base import BaseHandler

from models.Post import Post
import datetime

class PostsHandler(BaseHandler):
    def get(self):
        template_values = {
            'posts': []
        }

        posts = Post.query().order(-Post.created)

        for post in posts:
            template_values['posts'].append({
                'title': post.title,
                'content': post.content,
                'created': post.created.strftime('%B %d, %Y'),
                'id': post.key.id(),
            })

        print template_values


        self.render('index', template_values)
