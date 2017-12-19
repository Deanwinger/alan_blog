import app

db = app.dbs

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.username