from google.appengine.ext import ndb

class User(ndb.Model):
    username = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    email = ndb.StringProperty()
    password = ndb.StringProperty()
    modified = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def exists(cls, username):
        get_one = cls.query(User.username == username).fetch(1)
        return bool(get_one)
