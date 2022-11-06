from flask_security import UserMixin
from werkzeug.security import check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))

    def check_password(self, password):
        # return verify_password(self.password, password)   # from Flask-Security
        # return verify_and_update_password(self.password, password) # from Flask-Security
        return check_password(self.password, password) # from werkzeug.security