from . import db
class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    age = db.Column(db.String(120))
    image = db.Column(db.String(120))
    sex = db.Column(db.String(1))
    
    username = db.Column(db.String(80), unique=True)
    password=db.Column(db.String(255))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
    def __init__(self, firstname, lastname, age, image, sex):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.image = image
        self.sex = sex

    def __repr__(self):
        return '<User %r>' % (self.firstname)
