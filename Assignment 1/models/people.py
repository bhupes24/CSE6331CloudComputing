from flask_sqlalchemy import SQLAlchemy

db =SQLAlchemy()

class PeopleModel(db.Model):
    __tablename__ = "people"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    state = db.Column(db.Text)
    salary = db.Column(db.Integer)
    grade = db.Column(db.SmallInteger)
    room = db.Column(db.SmallInteger)
    telnum = db.Column(db.Integer)
    picture = db.Column(db.Text)
    keywords = db.Column(db.Text)

    def __init__(self, name, state, salary, grade, room, telnum, picture, keywords):
        # self.id = id
        self.name = name
        self.state = state
        self.salary = salary
        self.grade = grade
        self.room = room
        self.telnum = telnum
        self.picture = picture
        self.keywords = keywords

    def __repr__(self):
        return f"'id':{self.id}, 'name':{self.name}, 'keywords':{self.keywords}, 'salary':{self.salary}, 'picture':{self.picture}"

