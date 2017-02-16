from google.appengine.ext import ndb

# TODO make sure it is owned by a user
class Post(ndb.Model):
    title = ndb.StringProperty(required = True)
    content = ndb.TextProperty(required = True)
    created = ndb.DateTimeProperty(auto_now_add = True)
    modified = ndb.DateTimeProperty(auto_now = True)

    # @classmethod
    # def get_all_yo(cls):
    #     return cls.query().fetch(100)
