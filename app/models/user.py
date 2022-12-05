from app.extensions import db 
from flask_login import userMixin 
from werkzeug.security import generate_password_hash, check_password_hash




@property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)