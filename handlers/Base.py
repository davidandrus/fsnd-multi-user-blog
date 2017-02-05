import webapp2
import jinja2
from os import path

JINJA_TEMPLATE_PATH = path.join(path.dirname(__file__), '../', 'templates')
JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(JINJA_TEMPLATE_PATH),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseHandler(webapp2.RequestHandler):
    """A Base Request handler"""
    def render(self, template, t_vars):
        template = JINJA_ENV.get_template(template + '.html.j2')
        rendered = template.render(t_vars)
        self.response.write(rendered)
